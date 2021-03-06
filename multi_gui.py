import os
import subprocess
import sys
from pathlib import Path

import multitable

DEBUG = False

if DEBUG:
    from PyQt5 import uic

from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QListWidgetItem, QAbstractItemView

# This is to make sure that multitable finds the application path even when it is
# executed from another path e.g. when opened via "open file" in windows:

if getattr(sys, 'frozen', False):
    # If the application is run as a bundle, the pyInstaller bootloader
    # extends the sys module by a flag frozen=True and sets the app
    # path into variable _MEIPASS'.
    application_path = sys._MEIPASS
else:
    application_path = os.path.dirname(os.path.abspath(__file__))


class AppWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MultitableWindow()
        self.ui.setupUi(self)
        self.ui.report_button.setDisabled(True)
        self.ui.removeButton.setDisabled(True)
        self.connect_signals_and_slots()
        # Important for Drag&Drop action without delete:
        self.ui.CifFileListListWidget.setDragDropMode(QAbstractItemView.InternalMove)

    def connect_signals_and_slots(self):
        self.ui.cif_files_button.clicked.connect(self.add_files_to_list)
        self.ui.removeButton.clicked.connect(self.remove_file)
        self.ui.report_button.clicked.connect(self.make_report)
        self.ui.CifFileListListWidget.itemClicked.connect(self.toggle_remove)

    def toggle_remove(self, selection):
        selected = False
        for num in range(0, self.ui.CifFileListListWidget.count()):
            if self.ui.CifFileListListWidget.item(num).isSelected():
                selected = True
        if selected:
            self.ui.removeButton.setEnabled(True)
        else:
            self.ui.removeButton.setDisabled(True)

    def add_files_to_list(self, files=None):
        """
        Add files to the files list.
        """
        # self.ui.CifFileListListWidget.clear()  # make multiple add possible.
        if not files:
            files = self.get_files_from_dialog()
        if files:
            # self.ui.removeButton.setEnabled(True)
            self.ui.report_button.setEnabled(True)
        else:
            return
        for n, file in enumerate(files):
            if file:
                cif_tree_item = QListWidgetItem()
                self.ui.CifFileListListWidget.addItem(cif_tree_item)
                cif_tree_item.setText(file)

    def remove_file(self):
        """
        Removes the currently selected file from list.
        """
        sel = self.ui.CifFileListListWidget.selectionModel().selection()
        for s in sel.indexes():
            self.ui.CifFileListListWidget.takeItem(s.row())

    def get_files_from_dialog(self):
        """
        Returns the cif files from a file dialog.
        """
        ciffiles, _ = QFileDialog.getOpenFileNames(filter='CIF files (*.cif, *.CIF);; All Files (*.*,)',
                                                   # initialFilter='*.cif, *.CIF',
                                                   caption='Open .cif Files')
        # print(ciffiles)
        return ciffiles

    def open_report_document(self, report_filename: str):
        if Path(report_filename).absolute().exists():
            if os.name == 'nt':
                os.startfile(Path(report_filename).absolute())
            if sys.platform == 'darwin':
                subprocess.call(['open', Path(report_filename).absolute()])

    def make_report(self):
        files_list = []
        self.ui.OutputTextEdit.clear()
        for num in range(self.ui.CifFileListListWidget.count()):
            item = self.ui.CifFileListListWidget.item(num)
            itemtxt = item.text()
            files_list.append(Path(itemtxt))
            self.ui.OutputTextEdit.append(Path(itemtxt).name)
        if not files_list:
            return
        output_filename, _ = QFileDialog.getSaveFileName(filter='MS Word Documents (*.docx);;',
                                                         caption="Save Table To",
                                                         directory='./multitable.docx')
        # initialFilter='*.docx')
        multitable.make_report_from(files_list, output_filename)
        self.ui.OutputTextEdit.append('\nReport finished - output file: {}'.format(output_filename))
        self.open_report_document(output_filename)
        self.ui.CifFileListListWidget.clear()


if __name__ == '__main__':
    if DEBUG:
        uic.compileUiDir(os.path.join(application_path, './gui'))
    from gui.mainwindow import Ui_MultitableWindow

    app = QApplication(sys.argv)
    w = AppWindow()
    w.show()
    sys.exit(app.exec_())
