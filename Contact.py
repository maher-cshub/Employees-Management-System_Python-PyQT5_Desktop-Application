from PyQt5.QtWidgets import QApplication, QMainWindow,QMessageBox
from PyQt5.uic import loadUi
import BACKEND.SignIn, BACKEND.SignUp, BACKEND.Validation, BACKEND.EmployeeManipulate, BACKEND.PayementsManipulate,BACKEND.PresenceManipulate
import sys

MAIN_UI = "./UI"


class Main(QMainWindow):
    def __init__(self):
        super(Main,self).__init__()
        loadUi(f"{MAIN_UI}/contact_window.ui",self)
        self.setFixedSize(500,700)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    ##window.showMaximized()
    app.exec_()
