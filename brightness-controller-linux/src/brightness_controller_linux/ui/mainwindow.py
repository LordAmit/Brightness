# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindowlPqlsB.ui'
##
## Created by: Qt User Interface Compiler version 5.15.5
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

#from PySide2.QtCore import *  # type: ignore
#from PySide2.QtGui import *  # type: ignore
#from PySide2.QtWidgets import *  # type: ignore

from qtpy.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from qtpy.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from qtpy.QtWidgets import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(701, 340)
        MainWindow.setMinimumSize(QSize(701, 340))
        MainWindow.setMaximumSize(QSize(701, 340))
        MainWindow.setDocumentMode(True)
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.actionHelp = QAction(MainWindow)
        self.actionHelp.setObjectName(u"actionHelp")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionLicense = QAction(MainWindow)
        self.actionLicense.setObjectName(u"actionLicense")
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        self.actionSave.setVisible(True)
        self.actionLoad = QAction(MainWindow)
        self.actionLoad.setObjectName(u"actionLoad")
        self.actionLoad.setVisible(True)
        self.actionCheck_for_update = QAction(MainWindow)
        self.actionCheck_for_update.setObjectName(u"actionCheck_for_update")
        self.actionCheck_for_update.setEnabled(False)
        self.actionDefault = QAction(MainWindow)
        self.actionDefault.setObjectName(u"actionDefault")
        self.actionClearDefault = QAction(MainWindow)
        self.actionClearDefault.setObjectName(u"actionClearDefault")
        self.actionClearDefault.setVisible(False)
        self.centralWidget = QWidget(MainWindow)
        self.centralWidget.setObjectName(u"centralWidget")
        self.horizontalLayoutWidget = QWidget(self.centralWidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 0, 511, 261))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.groupBox_2 = QGroupBox(self.horizontalLayoutWidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.horizontalLayoutWidget_2 = QWidget(self.groupBox_2)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(10, 40, 231, 211))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.primary_brightness = QSlider(self.horizontalLayoutWidget_2)
        self.primary_brightness.setObjectName(u"primary_brightness")
        self.primary_brightness.setValue(99)
        self.primary_brightness.setOrientation(Qt.Vertical)

        self.horizontalLayout_2.addWidget(self.primary_brightness)

        self.primary_red = QSlider(self.horizontalLayoutWidget_2)
        self.primary_red.setObjectName(u"primary_red")
        self.primary_red.setValue(99)
        self.primary_red.setOrientation(Qt.Vertical)

        self.horizontalLayout_2.addWidget(self.primary_red)

        self.primary_green = QSlider(self.horizontalLayoutWidget_2)
        self.primary_green.setObjectName(u"primary_green")
        self.primary_green.setValue(99)
        self.primary_green.setOrientation(Qt.Vertical)

        self.horizontalLayout_2.addWidget(self.primary_green)

        self.primary_blue = QSlider(self.horizontalLayoutWidget_2)
        self.primary_blue.setObjectName(u"primary_blue")
        self.primary_blue.setValue(99)
        self.primary_blue.setOrientation(Qt.Vertical)

        self.horizontalLayout_2.addWidget(self.primary_blue)


        self.horizontalLayout.addWidget(self.groupBox_2)

        self.groupBox = QGroupBox(self.horizontalLayoutWidget)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayoutWidget_3 = QWidget(self.groupBox)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(20, 40, 231, 211))
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.secondary_brightness = QSlider(self.horizontalLayoutWidget_3)
        self.secondary_brightness.setObjectName(u"secondary_brightness")
        self.secondary_brightness.setValue(99)
        self.secondary_brightness.setOrientation(Qt.Vertical)

        self.horizontalLayout_3.addWidget(self.secondary_brightness)

        self.secondary_red = QSlider(self.horizontalLayoutWidget_3)
        self.secondary_red.setObjectName(u"secondary_red")
        self.secondary_red.setContextMenuPolicy(Qt.CustomContextMenu)
        self.secondary_red.setValue(99)
        self.secondary_red.setOrientation(Qt.Vertical)

        self.horizontalLayout_3.addWidget(self.secondary_red)

        self.secondary_green = QSlider(self.horizontalLayoutWidget_3)
        self.secondary_green.setObjectName(u"secondary_green")
        self.secondary_green.setValue(99)
        self.secondary_green.setOrientation(Qt.Vertical)

        self.horizontalLayout_3.addWidget(self.secondary_green)

        self.secondary_blue = QSlider(self.horizontalLayoutWidget_3)
        self.secondary_blue.setObjectName(u"secondary_blue")
        self.secondary_blue.setValue(99)
        self.secondary_blue.setOrientation(Qt.Vertical)

        self.horizontalLayout_3.addWidget(self.secondary_blue)


        self.horizontalLayout.addWidget(self.groupBox)

        self.label = QLabel(self.centralWidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 260, 71, 16))
        self.label_2 = QLabel(self.centralWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(100, 260, 21, 16))
        self.label_3 = QLabel(self.centralWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(150, 260, 21, 16))
        self.label_4 = QLabel(self.centralWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(200, 260, 16, 16))
        self.label_5 = QLabel(self.centralWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(290, 260, 71, 16))
        self.label_6 = QLabel(self.centralWidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(370, 260, 21, 16))
        self.label_7 = QLabel(self.centralWidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(420, 260, 21, 16))
        self.label_8 = QLabel(self.centralWidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(470, 260, 16, 16))
        self.verticalLayoutWidget = QWidget(self.centralWidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(529, 0, 218, 258))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.verticalLayoutWidget)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout.addWidget(self.label_9)

        self.label_12 = QLabel(self.verticalLayoutWidget)
        self.label_12.setObjectName(u"label_12")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.label_12)

        self.primary_combobox = QComboBox(self.verticalLayoutWidget)
        self.primary_combobox.setObjectName(u"primary_combobox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.primary_combobox.sizePolicy().hasHeightForWidth())
        self.primary_combobox.setSizePolicy(sizePolicy1)
        self.primary_combobox.setMaximumSize(QSize(150, 28))

        self.verticalLayout.addWidget(self.primary_combobox)

        self.label_11 = QLabel(self.verticalLayoutWidget)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout.addWidget(self.label_11)

        self.secondary_combo = QComboBox(self.verticalLayoutWidget)
        self.secondary_combo.setObjectName(u"secondary_combo")
        self.secondary_combo.setMaximumSize(QSize(150, 28))

        self.verticalLayout.addWidget(self.secondary_combo)

        self.label_10 = QLabel(self.verticalLayoutWidget)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout.addWidget(self.label_10)

        self.comboBox = QComboBox(self.verticalLayoutWidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMaximumSize(QSize(150, 28))

        self.verticalLayout.addWidget(self.comboBox)

        self.ddcutilsNotInstalled = QLabel(self.verticalLayoutWidget)
        self.ddcutilsNotInstalled.setObjectName(u"ddcutilsNotInstalled")
        self.ddcutilsNotInstalled.setEnabled(True)
        font = QFont()
        font.setPointSize(8)
        self.ddcutilsNotInstalled.setFont(font)

        self.verticalLayout.addWidget(self.ddcutilsNotInstalled)

        self.directControlBox = QCheckBox(self.verticalLayoutWidget)
        self.directControlBox.setObjectName(u"directControlBox")
        self.directControlBox.setEnabled(False)

        self.verticalLayout.addWidget(self.directControlBox)

        MainWindow.setCentralWidget(self.centralWidget)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 701, 32))
        self.menuFile = QMenu(self.menuBar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuHelp = QMenu(self.menuBar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menuBar)

        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionDefault)
        self.menuFile.addAction(self.actionClearDefault)
        self.menuFile.addAction(self.actionLoad)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionHelp)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionLicense)
        self.menuHelp.addAction(self.actionCheck_for_update)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Brightness Controller", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"E&xit", None))
        self.actionHelp.setText(QCoreApplication.translate("MainWindow", u"&Help", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"&About", None))
        self.actionLicense.setText(QCoreApplication.translate("MainWindow", u"&License", None))
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"&Save current settings", None))
        self.actionLoad.setText(QCoreApplication.translate("MainWindow", u"&Load settings", None))
        self.actionCheck_for_update.setText(QCoreApplication.translate("MainWindow", u"&Check for Update", None))
        self.actionDefault.setText(QCoreApplication.translate("MainWindow", u"Save current as default", None))
        self.actionClearDefault.setText(QCoreApplication.translate("MainWindow", u"&Clear default settings", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Primary", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Secondary", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Brightness", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u" R", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u" G", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u" B", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Brightness", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u" R", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u" G", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u" B", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Advanced", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Primary Brightness", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Secondary Brightness", None))
#if QT_CONFIG(tooltip)
        self.secondary_combo.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>You can select the source of Secondary Brightness Here.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Color Temperature", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Default", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"1900K Candle", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"2600K 40W Tungsten", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"2850K 100W Tungsten", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"3200K Halogen", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"5200K Carbon Arc", None))
        self.comboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"5400K High Noon", None))
        self.comboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"6000K Direct Sun", None))
        self.comboBox.setItemText(8, QCoreApplication.translate("MainWindow", u"7000K Overcast Sky", None))
        self.comboBox.setItemText(9, QCoreApplication.translate("MainWindow", u"20000K Clear Blue Sky", None))

        self.ddcutilsNotInstalled.setText(QCoreApplication.translate("MainWindow", u"Install ddcutil for direct control", None))
        self.directControlBox.setText(QCoreApplication.translate("MainWindow", u"Direct Control (DDC)", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"&File", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"&Help", None))
    # retranslateUi

