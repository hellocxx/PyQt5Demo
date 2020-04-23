import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5.QtGui import QIcon

class FirstMainWin(QMainWindow):
    def __init__(self,parent=None):
        super(FirstMainWin,self).__init__(parent)
        #设置主窗口的标题
        self.setWindowTitle('第一个主窗口应用')

        #设置窗口的尺寸
        self.resize(400,300)

        self.status = self.statusBar()
        self.status.showMessage('只停留5秒的消息',5000)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    app.setWindowIcon(QIcon('material/icoASK.ico'))
    main = FirstMainWin()
    main.show()
    sys.exit(app.exec_())
