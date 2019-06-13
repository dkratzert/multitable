import os
import sys
from pathlib import Path

DEBUG = True

if DEBUG:
    from PyQt5 import uic

from PyQt5.QtWidgets import QMainWindow, QApplication, QHeaderView, QTableWidget

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


class AppWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_FinalizerWindow()
        self.ui.setupUi(self)
        # distribute CifItemsTable Columns evenly:
        header = self.ui.CifItemsTable.horizontalHeader()
        header.setSectionResizeMode(1, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(0, QHeaderView.Stretch)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = AppWindow()
    w.showMaximized()
    sys.exit(app.exec_())
