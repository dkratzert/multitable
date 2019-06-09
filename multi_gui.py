import os
import sys
from pathlib import Path

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QTreeWidgetItem

# This is to make sure that multitable finds the application path even when it is
# executed from another path e.g. when opened via "open file" in windows:
import multitable

if getattr(sys, 'frozen', False):
    # If the application is run as a bundle, the pyInstaller bootloader
    # extends the sys module by a flag frozen=True and sets the app
    # path into variable _MEIPASS'.
    application_path = sys._MEIPASS
else:
    application_path = os.path.dirname(os.path.abspath(__file__))


# TODO: exit button

class AppWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MultitableWindow()
        self.ui.setupUi(self)
        self.show()
        self.ui.report_button.setDisabled(True)
        self.ui.removeButton.setDisabled(True)
        self.connect_signals_and_slots()
        self.ui.CifFileListTreeWidget.resizeColumnToContents(0)

    def connect_signals_and_slots(self):
        self.ui.cif_files_button.clicked.connect(self.add_files_to_list)
        self.ui.removeButton.clicked.connect(self.remove_file)
        self.ui.report_button.clicked.connect(self.make_report)
        self.ui.CifFileListTreeWidget.itemClicked.connect(self.toggle_remove)

    def toggle_remove(self, selection):
        selected = False
        for num in range(0, self.ui.CifFileListTreeWidget.topLevelItemCount()):
            if self.ui.CifFileListTreeWidget.topLevelItem(num).isSelected():
                selected = True
        if selected == True:
            self.ui.removeButton.setEnabled(True)
        else:
            self.ui.removeButton.setDisabled(True)

    def add_files_to_list(self, files=None):
        """
        Add files to the files list.
        """
        self.ui.CifFileListTreeWidget.clear()
        if not files:
            files = self.get_files_from_dialog()
        if files:
            #self.ui.removeButton.setEnabled(True)
            self.ui.report_button.setEnabled(True)
        else:
            return
        for n, file in enumerate(files):
            if file:
                cif_tree_item = QTreeWidgetItem()
                self.ui.CifFileListTreeWidget.addTopLevelItem(cif_tree_item)
                cif_tree_item.setText(0, file)
                #cif_tree_item.currentItemChanged.connect(self.toggle_remove("selected"))
                # button = QPushButton("remove")
                # self.ui.CifFileListTreeWidget.setItemWidget(cif_tree_item, 1, button)
                # button.setMinimumWidth(80)
                # button.setMaximumWidth(80)
                # button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
                # button.clicked.connect(self.remove_file)
        self.ui.CifFileListTreeWidget.resizeColumnToContents(0)

    def remove_file(self):
        """
        Removes the currently selected file from list.
        """
        sel = self.ui.CifFileListTreeWidget.selectionModel().selection()
        if sel.indexes()[0]:
            self.ui.CifFileListTreeWidget.takeTopLevelItem(sel.indexes()[0].row())

    def get_files_from_dialog(self):
        """
        Returns the cif files from a file dialog.
        """
        ciffiles, _ = QFileDialog.getOpenFileNames(filter='*.cif')
        # print(ciffiles)
        return ciffiles

    def make_report(self):
        files_list = []
        self.ui.OutputTextEdit.clear()
        for num in range(self.ui.CifFileListTreeWidget.topLevelItemCount()):
            item = self.ui.CifFileListTreeWidget.topLevelItem(num)
            itemtxt = item.text(0)
            files_list.append(itemtxt)
            self.ui.OutputTextEdit.append(Path(itemtxt).name)
        if not files_list:
            return 
        multitable.make_report_from(files_list)
        self.ui.OutputTextEdit.append('\nReport finished - output file: multitable.docx')
        self.ui.CifFileListTreeWidget.clear()


if __name__ == '__main__':
    uic.compileUiDir(os.path.join(application_path, './gui'))
    from gui.mainwindow import Ui_MultitableWindow
    app = QApplication(sys.argv)
    w = AppWindow()
    w.show()
    sys.exit(app.exec_())
