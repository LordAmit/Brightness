#!/usr/bin/python
# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-
### BEGIN LICENSE
# This file is in the public domain
### END LICENSE

import sys
import os.path
import unittest
sys.path.insert(0, os.path.realpath(os.path.join(os.path.dirname(__file__), "..")))

from brightness_controller import AboutBrightnessControllerDialog

class TestExample(unittest.TestCase):
    def setUp(self):
        self.AboutBrightnessControllerDialog_members = [
        'AboutDialog', 'AboutBrightnessControllerDialog', 'gettext', 'logger', 'logging']

    def test_AboutBrightnessControllerDialog_members(self):
        all_members = dir(AboutBrightnessControllerDialog)
        public_members = [x for x in all_members if not x.startswith('_')]
        public_members.sort()
        self.assertEqual(self.AboutBrightnessControllerDialog_members, public_members)

if __name__ == '__main__':    
    unittest.main()
