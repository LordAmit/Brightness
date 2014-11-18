# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-
### BEGIN LICENSE
# This file is in the public domain
### END LICENSE

import locale
from locale import gettext as _
locale.textdomain('brightness_controller')

import subprocess
from gi.repository import Gtk, WebKit # pylint: disable=E0611
import logging
logger = logging.getLogger('brightness_controller')

from brightness_controller_lib import Window
from brightness_controller_lib.helpers import get_media_file


# See brightness_controller_lib.Window.py for more details about how this class works
class BrightnessControllerWindow(Window):
    __gtype_name__ = "BrightnessControllerWindow"
    
    def finish_initializing(self, builder): # pylint: disable=E1002
        """Set up the main window"""
        super(BrightnessControllerWindow, self).finish_initializing(builder)
        self.box = self.builder.get_object("box")
        self.window = self.builder.get_object("brightness_controller")
        self.drag = True
        self.set_opacity(0.7)

        # Code for other initialization actions should be added here.
        self.webview = WebKit.WebView()
        self.box.add(self.webview)
        self.webview.props.settings.enable_default_context_menu = False
        self.webviewsettings = self.webview.get_settings()
        self.webviewsettings.set_property("javascript-can-open-windows-automatically", True)
        self.webviewsettings.set_property("enable-universal-access-from-file-uris", True)
        self.webviewsettings.set_property('enable-default-context-menu',False)
        self.webview.load_uri(get_media_file('index.html'))
        self.box.show_all()

        try:
            launcher = Unity.LauncherEntry.get_for_desktop_id("brightness-controller.desktop")
            launcher.set_property("count_visible", False)
        except NameError:
            pass

        def navigation_requested_cb(view, frame, networkRequest):
            uri = networkRequest.get_uri()
            subprocess.Popen(['xdg-open', uri])
            return 1

        def console_message_cb(widget, message, line, source):
            logger.debug('%s:%s "%s"' % (source, line, message))
            return True

        def title_changed(widget, frame, title):
            print title
            if title == "close":
                Gtk.main_quit()
            elif title == "minimize":
                self.iconify()

            # Disables Dragging
            elif title == "disable_drag":
                self.drag = False
            elif title == "enable_drag":
                self.drag = True

            else:
                try:
                    subprocess.call(title,shell=True)
                except NameError:
                    print "Some error has occured. Report a bug at http://github.com/lordamit/brightness.git"

        def press_button(widget, event):
            if event.button == 1:
                if self.drag == True:
                    try:
                        Gtk.Window.begin_move_drag(self, event.button, event.x_root, event.y_root, event.time)
                    except TypeError:
                        pass

        self.webview.connect('title-changed', title_changed)
        self.webview.connect('navigation-requested', navigation_requested_cb)
        self.webview.connect('console-message', console_message_cb)
        self.webview.connect('button-press-event', press_button)
