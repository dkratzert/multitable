# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/daniel/GitHub/multitable/./gui/mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MultitableWindow(object):
    def setupUi(self, MultitableWindow):
        MultitableWindow.setObjectName("MultitableWindow")
        MultitableWindow.resize(745, 511)
        self.Mainwidget = QtWidgets.QWidget(MultitableWindow)
        self.Mainwidget.setObjectName("Mainwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.Mainwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.report_button = QtWidgets.QPushButton(self.Mainwidget)
        self.report_button.setObjectName("report_button")
        self.gridLayout.addWidget(self.report_button, 0, 1, 1, 1)
        self.cif_files_button = QtWidgets.QPushButton(self.Mainwidget)
        self.cif_files_button.setObjectName("cif_files_button")
        self.gridLayout.addWidget(self.cif_files_button, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 2, 1, 1)
        self.removeButton = QtWidgets.QPushButton(self.Mainwidget)
        self.removeButton.setObjectName("removeButton")
        self.gridLayout.addWidget(self.removeButton, 0, 3, 1, 1)
        self.splitter = QtWidgets.QSplitter(self.Mainwidget)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.CifFileListTreeWidget = QtWidgets.QTreeWidget(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(4)
        sizePolicy.setHeightForWidth(self.CifFileListTreeWidget.sizePolicy().hasHeightForWidth())
        self.CifFileListTreeWidget.setSizePolicy(sizePolicy)
        self.CifFileListTreeWidget.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.CifFileListTreeWidget.setItemsExpandable(True)
        self.CifFileListTreeWidget.setObjectName("CifFileListTreeWidget")
        self.CifFileListTreeWidget.header().setVisible(False)
        self.OutputTextEdit = QtWidgets.QTextEdit(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.OutputTextEdit.sizePolicy().hasHeightForWidth())
        self.OutputTextEdit.setSizePolicy(sizePolicy)
        self.OutputTextEdit.setMinimumSize(QtCore.QSize(0, 0))
        self.OutputTextEdit.setReadOnly(True)
        self.OutputTextEdit.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.OutputTextEdit.setObjectName("OutputTextEdit")
        self.gridLayout.addWidget(self.splitter, 1, 0, 1, 4)
        MultitableWindow.setCentralWidget(self.Mainwidget)
        self.menubar = QtWidgets.QMenuBar(MultitableWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 745, 22))
        self.menubar.setObjectName("menubar")
        MultitableWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MultitableWindow)
        self.statusbar.setObjectName("statusbar")
        MultitableWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MultitableWindow)
        QtCore.QMetaObject.connectSlotsByName(MultitableWindow)

    def retranslateUi(self, MultitableWindow):
        _translate = QtCore.QCoreApplication.translate
        MultitableWindow.setWindowTitle(_translate("MultitableWindow", "MainWindow"))
        self.report_button.setText(_translate("MultitableWindow", "Generate Report"))
        self.cif_files_button.setText(_translate("MultitableWindow", "Select CIF files"))
        self.removeButton.setText(_translate("MultitableWindow", "Remove Current File"))
        self.CifFileListTreeWidget.setSortingEnabled(True)


