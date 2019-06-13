import os
import sys

DEBUG = True

if DEBUG:
    from PyQt5 import uic

from PyQt5.QtWidgets import QMainWindow, QApplication, QHeaderView, QLineEdit, QLabel, QPushButton

if getattr(sys, 'frozen', False):
    # If the application is run as a bundle, the pyInstaller bootloader
    # extends the sys module by a flag frozen=True and sets the app
    # path into variable _MEIPASS'.
    application_path = sys._MEIPASS
else:
    application_path = os.path.dirname(os.path.abspath(__file__))

if DEBUG:
    uic.compileUiDir(os.path.join(application_path, './gui'))
from gui.finalizer import Ui_FinalizerWindow


"""
TODO:

- the working directory has to be the directory of the currently opened cif file
- open cif file and parse it. (With gemmi?)
- put all incomplete information in the CifItemsTable. 
  - Add checkbox to be able to edit all cif values?
  - Or show all ? items first, then all others.
- make first and second column of CifItemsTable uneditable.
- Own data in CifItemsTable overrides From Data Source. 
  (maybe with a signal to grey out the data source onEdit of Own Data)
- make "save cif" work.
- think about a possibility to save and edit templates: QSettings()
- signal: if edit template clicked -> got to TemplatesStackedWidgetPage1
- signal: if Save template clicked -> got to TemplatesStackedWidgetPage0
- signal: if delete clicked -> delete current template table line
- signal: if edit Own Data field -> grey out From Data Source field in same line.
- action: rightclick on a template -> offer "delete template"
- action: rightclick on a template -> offer "export template (to .cif)"
- action: rightclick on a template -> offer "import template (from .cif)"
- selecting a row in the cif items table changes the view in the Data Sources table and offers
  possible files as data sources. For example a .abs file for Tmin/Tmax
- method: clear_data_sources_list() -> clear all in DataFilesGroupBox
- get correct Rint, Tmin/Tmax from twinabs by combining reflections count with modification time, 
  domain count?, hkl type
- SaveResidualsTableButton -> run multitable.py
- SaveFullReportButton -> generate full report with description text and all tables as .docx (and pdf?)
  maybe also a preview? Directly open in MSword/LibreOffice?

- save cif file with "name_fin.cif"

- Add button for checkcif report.

"""


class AppWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_FinalizerWindow()
        self.ui.setupUi(self)
        self.show()
        # distribute CifItemsTable Columns evenly:
        hheader = self.ui.CifItemsTable.horizontalHeader()
        hheader.setSectionResizeMode(0, QHeaderView.Stretch)
        hheader.setSectionResizeMode(1, QHeaderView.Stretch)
        hheader.setSectionResizeMode(2, QHeaderView.Stretch)
        hheader.setAlternatingRowColors(True)

    def add_new_datafile(self, n: int, label_text: str, placeholder: str = ''):
        """
        Adds a new file input as data source for the currently selected cif key/value pair
        """
        data_file_label = QLabel(self.DataFilesGroupBox)
        data_file_label.setText(label_text)
        data_file_edit = QLineEdit(self.ui.DataFilesGroupBox)
        data_file_edit.setPlaceholderText(placeholder)
        data_file_button = QPushButton(self.DataFilesGroupBox)
        data_file_button.setText('Select File')
        self.ui.DataSourcesGridLayout.addWidget(data_file_label, n, 0, 1, 1)
        self.ui.DataSourcesGridLayout.addWidget(data_file_edit, n, 1, 1, 1)
        self.ui.DataSourcesGridLayout.addWidget(data_file_button, n, 2, 1, 1)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = AppWindow()
    w.showMaximized()
    sys.exit(app.exec_())
