# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\GitHub\multitable\./gui\mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MultitableWindow(object):
    def setupUi(self, MultitableWindow):
        MultitableWindow.setObjectName("MultitableWindow")
        MultitableWindow.resize(809, 588)
        self.Mainwidget = QtWidgets.QWidget(MultitableWindow)
        self.Mainwidget.setObjectName("Mainwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.Mainwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.cif_files_button = QtWidgets.QPushButton(self.Mainwidget)
        self.cif_files_button.setObjectName("cif_files_button")
        self.gridLayout.addWidget(self.cif_files_button, 0, 0, 1, 1)
        self.report_button = QtWidgets.QPushButton(self.Mainwidget)
        self.report_button.setObjectName("report_button")
        self.gridLayout.addWidget(self.report_button, 0, 1, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 3, 1, 1)
        self.removeButton = QtWidgets.QPushButton(self.Mainwidget)
        self.removeButton.setObjectName("removeButton")
        self.gridLayout.addWidget(self.removeButton, 0, 4, 1, 1)
        self.splitter_2 = QtWidgets.QSplitter(self.Mainwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter_2.sizePolicy().hasHeightForWidth())
        self.splitter_2.setSizePolicy(sizePolicy)
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.groupBox = QtWidgets.QGroupBox(self.splitter_2)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.CifFileListListWidget = QtWidgets.QListWidget(self.groupBox)
        self.CifFileListListWidget.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
        self.CifFileListListWidget.setDefaultDropAction(QtCore.Qt.CopyAction)
        self.CifFileListListWidget.setAlternatingRowColors(True)
        self.CifFileListListWidget.setObjectName("CifFileListListWidget")
        self.verticalLayout.addWidget(self.CifFileListListWidget)
        self.groupBox_2 = QtWidgets.QGroupBox(self.splitter_2)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.OutputTextEdit = QtWidgets.QTextEdit(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.OutputTextEdit.sizePolicy().hasHeightForWidth())
        self.OutputTextEdit.setSizePolicy(sizePolicy)
        self.OutputTextEdit.setMinimumSize(QtCore.QSize(0, 0))
        self.OutputTextEdit.setReadOnly(True)
        self.OutputTextEdit.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.OutputTextEdit.setObjectName("OutputTextEdit")
        self.verticalLayout_2.addWidget(self.OutputTextEdit)
        self.gridLayout.addWidget(self.splitter_2, 1, 0, 2, 5)
        MultitableWindow.setCentralWidget(self.Mainwidget)

        self.retranslateUi(MultitableWindow)
        QtCore.QMetaObject.connectSlotsByName(MultitableWindow)

    def retranslateUi(self, MultitableWindow):
        _translate = QtCore.QCoreApplication.translate
        MultitableWindow.setWindowTitle(_translate("MultitableWindow", "Mutitable"))
        self.cif_files_button.setText(_translate("MultitableWindow", "Select CIF files"))
        self.report_button.setText(_translate("MultitableWindow", "Generate Report"))
        self.removeButton.setToolTip(_translate("MultitableWindow", "<html><head/><body><p>Removes the currently selected file from the list.</p></body></html>"))
        self.removeButton.setText(_translate("MultitableWindow", "Remove Current File"))
        self.groupBox.setTitle(_translate("MultitableWindow", "Files List"))
        self.groupBox_2.setTitle(_translate("MultitableWindow", "Program Output"))


