# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\GitHub\multitable\./gui\finalizer.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FinalizerWindow(object):
    def setupUi(self, FinalizerWindow):
        FinalizerWindow.setObjectName("FinalizerWindow")
        FinalizerWindow.resize(1054, 671)
        self.Mainwidget = QtWidgets.QWidget(FinalizerWindow)
        self.Mainwidget.setObjectName("Mainwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.Mainwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.CifDataItemsGroupBox = QtWidgets.QGroupBox(self.Mainwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CifDataItemsGroupBox.sizePolicy().hasHeightForWidth())
        self.CifDataItemsGroupBox.setSizePolicy(sizePolicy)
        self.CifDataItemsGroupBox.setObjectName("CifDataItemsGroupBox")
        self.CifTableGridLayout = QtWidgets.QGridLayout(self.CifDataItemsGroupBox)
        self.CifTableGridLayout.setObjectName("CifTableGridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.CifTableGridLayout.addItem(spacerItem, 1, 1, 1, 1)
        self.SaveResidualsTableButton = QtWidgets.QPushButton(self.CifDataItemsGroupBox)
        self.SaveResidualsTableButton.setObjectName("SaveResidualsTableButton")
        self.CifTableGridLayout.addWidget(self.SaveResidualsTableButton, 2, 1, 1, 1)
        self.SaveFullReportButton = QtWidgets.QPushButton(self.CifDataItemsGroupBox)
        self.SaveFullReportButton.setObjectName("SaveFullReportButton")
        self.CifTableGridLayout.addWidget(self.SaveFullReportButton, 2, 2, 1, 1)
        self.CifItemsTable = QtWidgets.QTableWidget(self.CifDataItemsGroupBox)
        self.CifItemsTable.setMidLineWidth(0)
        self.CifItemsTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.CifItemsTable.setObjectName("CifItemsTable")
        self.CifItemsTable.setColumnCount(3)
        self.CifItemsTable.setRowCount(5)
        item = QtWidgets.QTableWidgetItem()
        self.CifItemsTable.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.CifItemsTable.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.CifItemsTable.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.CifItemsTable.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.CifItemsTable.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.CifItemsTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.CifItemsTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.CifItemsTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.CifItemsTable.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.CifItemsTable.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.CifItemsTable.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.CifItemsTable.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.CifItemsTable.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.CifItemsTable.setItem(2, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.CifItemsTable.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.CifItemsTable.setItem(4, 0, item)
        self.CifItemsTable.horizontalHeader().setHighlightSections(False)
        self.CifTableGridLayout.addWidget(self.CifItemsTable, 0, 0, 1, 3)
        self.SaveCifButton = QtWidgets.QPushButton(self.CifDataItemsGroupBox)
        self.SaveCifButton.setStyleSheet("background-color: rgb(70, 207, 70);")
        self.SaveCifButton.setObjectName("SaveCifButton")
        self.CifTableGridLayout.addWidget(self.SaveCifButton, 2, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.CifTableGridLayout.addItem(spacerItem1, 3, 1, 1, 1)
        self.gridLayout.addWidget(self.CifDataItemsGroupBox, 0, 1, 3, 1)
        self.CifFileGroupBox = QtWidgets.QGroupBox(self.Mainwidget)
        self.CifFileGroupBox.setObjectName("CifFileGroupBox")
        self.CifFileGridLayout = QtWidgets.QGridLayout(self.CifFileGroupBox)
        self.CifFileGridLayout.setObjectName("CifFileGridLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.CifFileGroupBox)
        self.lineEdit.setObjectName("lineEdit")
        self.CifFileGridLayout.addWidget(self.lineEdit, 0, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.CifFileGroupBox)
        self.pushButton.setObjectName("pushButton")
        self.CifFileGridLayout.addWidget(self.pushButton, 0, 1, 1, 1)
        self.gridLayout.addWidget(self.CifFileGroupBox, 0, 0, 1, 1)
        self.DataFilesGroupBox = QtWidgets.QGroupBox(self.Mainwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.DataFilesGroupBox.sizePolicy().hasHeightForWidth())
        self.DataFilesGroupBox.setSizePolicy(sizePolicy)
        self.DataFilesGroupBox.setObjectName("DataFilesGroupBox")
        self.DataSourcesGridLayout = QtWidgets.QGridLayout(self.DataFilesGroupBox)
        self.DataSourcesGridLayout.setObjectName("DataSourcesGridLayout")
        self.DataFileEdit = QtWidgets.QLineEdit(self.DataFilesGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DataFileEdit.sizePolicy().hasHeightForWidth())
        self.DataFileEdit.setSizePolicy(sizePolicy)
        self.DataFileEdit.setObjectName("DataFileEdit")
        self.DataSourcesGridLayout.addWidget(self.DataFileEdit, 1, 1, 1, 1)
        self.DataFileLabel = QtWidgets.QLabel(self.DataFilesGroupBox)
        self.DataFileLabel.setObjectName("DataFileLabel")
        self.DataSourcesGridLayout.addWidget(self.DataFileLabel, 1, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.DataSourcesGridLayout.addItem(spacerItem2, 2, 1, 1, 1)
        self.DataFileButton = QtWidgets.QPushButton(self.DataFilesGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DataFileButton.sizePolicy().hasHeightForWidth())
        self.DataFileButton.setSizePolicy(sizePolicy)
        self.DataFileButton.setObjectName("DataFileButton")
        self.DataSourcesGridLayout.addWidget(self.DataFileButton, 1, 2, 1, 1)
        self.gridLayout.addWidget(self.DataFilesGroupBox, 2, 0, 1, 1)
        self.TemplatesStackedWidget = QtWidgets.QStackedWidget(self.Mainwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.TemplatesStackedWidget.sizePolicy().hasHeightForWidth())
        self.TemplatesStackedWidget.setSizePolicy(sizePolicy)
        self.TemplatesStackedWidget.setObjectName("TemplatesStackedWidget")
        self.TemplatesStackedWidgetPage1 = QtWidgets.QWidget()
        self.TemplatesStackedWidgetPage1.setObjectName("TemplatesStackedWidgetPage1")
        self.TemplatesGridLayout = QtWidgets.QGridLayout(self.TemplatesStackedWidgetPage1)
        self.TemplatesGridLayout.setObjectName("TemplatesGridLayout")
        self.EditTemplateButton = QtWidgets.QPushButton(self.TemplatesStackedWidgetPage1)
        self.EditTemplateButton.setObjectName("EditTemplateButton")
        self.TemplatesGridLayout.addWidget(self.EditTemplateButton, 1, 1, 1, 1)
        self.TemplatesListWidget = QtWidgets.QListWidget(self.TemplatesStackedWidgetPage1)
        self.TemplatesListWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.TemplatesListWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.TemplatesListWidget.setObjectName("TemplatesListWidget")
        item = QtWidgets.QListWidgetItem()
        self.TemplatesListWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.TemplatesListWidget.addItem(item)
        self.TemplatesGridLayout.addWidget(self.TemplatesListWidget, 0, 0, 1, 2)
        self.NewTemplateButton = QtWidgets.QPushButton(self.TemplatesStackedWidgetPage1)
        self.NewTemplateButton.setObjectName("NewTemplateButton")
        self.TemplatesGridLayout.addWidget(self.NewTemplateButton, 1, 0, 1, 1)
        self.TemplatesStackedWidget.addWidget(self.TemplatesStackedWidgetPage1)
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.page)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.page)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_2.addWidget(self.pushButton_2, 1, 0, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.page)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_2.addWidget(self.pushButton_3, 1, 1, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(self.page)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(100)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.gridLayout_2.addWidget(self.tableWidget, 0, 0, 1, 2)
        self.TemplatesStackedWidget.addWidget(self.page)
        self.gridLayout.addWidget(self.TemplatesStackedWidget, 1, 0, 1, 1)
        FinalizerWindow.setCentralWidget(self.Mainwidget)
        self.actionSave_Report = QtWidgets.QAction(FinalizerWindow)
        self.actionSave_Report.setObjectName("actionSave_Report")
        self.actionSave_CIF_File = QtWidgets.QAction(FinalizerWindow)
        self.actionSave_CIF_File.setObjectName("actionSave_CIF_File")
        self.actionedit_templates = QtWidgets.QAction(FinalizerWindow)
        self.actionedit_templates.setObjectName("actionedit_templates")

        self.retranslateUi(FinalizerWindow)
        self.TemplatesStackedWidget.setCurrentIndex(0)
        self.EditTemplateButton.clicked.connect(self.EditTemplateButton.click)
        QtCore.QMetaObject.connectSlotsByName(FinalizerWindow)

    def retranslateUi(self, FinalizerWindow):
        _translate = QtCore.QCoreApplication.translate
        FinalizerWindow.setWindowTitle(_translate("FinalizerWindow", "Mutitable"))
        self.CifDataItemsGroupBox.setTitle(_translate("FinalizerWindow", "Missing CIF Items"))
        self.SaveResidualsTableButton.setText(_translate("FinalizerWindow", "Save Residuals Table"))
        self.SaveFullReportButton.setText(_translate("FinalizerWindow", "Save Full Report"))
        item = self.CifItemsTable.verticalHeaderItem(0)
        item.setText(_translate("FinalizerWindow", "_ls_refine_foo_bar"))
        item = self.CifItemsTable.verticalHeaderItem(1)
        item.setText(_translate("FinalizerWindow", "_exptl_absorpt_correction_T_max"))
        item = self.CifItemsTable.verticalHeaderItem(2)
        item.setText(_translate("FinalizerWindow", "_exptl_crystal_size_min"))
        item = self.CifItemsTable.verticalHeaderItem(3)
        item.setText(_translate("FinalizerWindow", "_diffrn_reflns_limit_l_max"))
        item = self.CifItemsTable.verticalHeaderItem(4)
        item.setText(_translate("FinalizerWindow", "_diffrn_ambient_temperature"))
        item = self.CifItemsTable.horizontalHeaderItem(0)
        item.setText(_translate("FinalizerWindow", "CIF Value"))
        item = self.CifItemsTable.horizontalHeaderItem(1)
        item.setText(_translate("FinalizerWindow", "From Data Source"))
        item = self.CifItemsTable.horizontalHeaderItem(2)
        item.setText(_translate("FinalizerWindow", "Own Data"))
        __sortingEnabled = self.CifItemsTable.isSortingEnabled()
        self.CifItemsTable.setSortingEnabled(False)
        item = self.CifItemsTable.item(0, 0)
        item.setText(_translate("FinalizerWindow", "foo"))
        item = self.CifItemsTable.item(0, 2)
        item.setText(_translate("FinalizerWindow", "bar"))
        item = self.CifItemsTable.item(1, 0)
        item.setText(_translate("FinalizerWindow", "?"))
        item = self.CifItemsTable.item(1, 1)
        item.setText(_translate("FinalizerWindow", "0.876"))
        item = self.CifItemsTable.item(2, 0)
        item.setText(_translate("FinalizerWindow", "?"))
        item = self.CifItemsTable.item(2, 2)
        item.setText(_translate("FinalizerWindow", "0.1"))
        item = self.CifItemsTable.item(3, 0)
        item.setText(_translate("FinalizerWindow", "13"))
        item = self.CifItemsTable.item(4, 0)
        item.setText(_translate("FinalizerWindow", "100"))
        self.CifItemsTable.setSortingEnabled(__sortingEnabled)
        self.SaveCifButton.setText(_translate("FinalizerWindow", "Save Cif File"))
        self.CifFileGroupBox.setTitle(_translate("FinalizerWindow", "Cif file"))
        self.lineEdit.setText(_translate("FinalizerWindow", "C:\\frames\\guest\\foo\\work\\bar.cif"))
        self.pushButton.setText(_translate("FinalizerWindow", "Select File"))
        self.DataFilesGroupBox.setTitle(_translate("FinalizerWindow", "Data Sources"))
        self.DataFileEdit.setPlaceholderText(_translate("FinalizerWindow", " .abs file from SADABS"))
        self.DataFileLabel.setText(_translate("FinalizerWindow", "SADABS"))
        self.DataFileButton.setText(_translate("FinalizerWindow", "Select File"))
        self.EditTemplateButton.setText(_translate("FinalizerWindow", "Edit Template"))
        __sortingEnabled = self.TemplatesListWidget.isSortingEnabled()
        self.TemplatesListWidget.setSortingEnabled(False)
        item = self.TemplatesListWidget.item(0)
        item.setText(_translate("FinalizerWindow", "Bruker D8 VENTURE"))
        item = self.TemplatesListWidget.item(1)
        item.setText(_translate("FinalizerWindow", "Bruker SMART APEXII QUAZAR"))
        self.TemplatesListWidget.setSortingEnabled(__sortingEnabled)
        self.NewTemplateButton.setText(_translate("FinalizerWindow", "New Template"))
        self.pushButton_2.setText(_translate("FinalizerWindow", "Save"))
        self.pushButton_3.setText(_translate("FinalizerWindow", "Delete"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("FinalizerWindow", "Key"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("FinalizerWindow", "Value"))
        self.actionSave_Report.setText(_translate("FinalizerWindow", "Save Report"))
        self.actionSave_CIF_File.setText(_translate("FinalizerWindow", "Save CIF File"))
        self.actionedit_templates.setText(_translate("FinalizerWindow", "edit templates"))


