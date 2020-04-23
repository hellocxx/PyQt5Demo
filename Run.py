#this is the main demo!!!
#PyQt5 + QTdesigner + PyUic + PyRcc + Pyinstaller

import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
import MainWinSignalAndSlot
if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = MainWinSignalAndSlot.Ui_MainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
  