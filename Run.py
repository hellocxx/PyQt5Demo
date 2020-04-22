#this is the main demo!!!
#PyQt5 + QTdesigner + PyUic + PyRcc + Pyinstaller

import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
import MainWinbuddyAndsunxv
if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = MainWinbuddyAndsunxv.Ui_MainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
