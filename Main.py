from PyQt5.QtWidgets import QApplication, QMainWindow,QMessageBox,QLineEdit
from PyQt5.uic import loadUi
from PyQt5.QtCore import QPropertyAnimation 
import BACKEND.SignIn, BACKEND.SignUp, BACKEND.Validation
import pickle
import sys
import os

MAIN_UI = "./UI"

##MAIN CLASS 
class Main(QMainWindow):
    def __init__(self):
        super(Main,self).__init__()
        loadUi(f"{MAIN_UI}/main_window.ui",self)
        ##UI LOADED
        self.password_connect.setEchoMode(QLineEdit.Password)
        self.connect_btn.clicked.connect(self.Connect_To_DB)
        self.register_btn.clicked.connect(self.Register_To_DB)
        self.setFixedSize(800, 600)

    def Info_Msg(self,info_title,info_text):
        msgBox1 = QMessageBox()
        msgBox1.setIcon(QMessageBox.Information)
        msgBox1.setWindowTitle(info_title)
        msgBox1.setText(info_text)
        msgBox1.setStandardButtons(QMessageBox.Ok)
        msgBox1.exec()
        return

    def Connect_To_DB(self):
        username = str(self.username_connect.toPlainText())
        password = str(self.password_connect.text())

        if(BACKEND.Validation.Isvalid_Password(password)==None):
            info_title = "Erreur"
            info_text = "Format Mot De Passe invalid \nMot De Passe doit avoir au moins 8 caracteres contenant (Maj,Min,Chiffre,Caractere Speciale (-@#$%^&+=_) "
            self.Info_Msg(info_title=info_title,info_text=info_text)
            return

        if(BACKEND.Validation.Isvalid_Username(username) == None):
            info_title = "Erreur"
            info_text = "Format Nom Utilisateur Invalid \nNom utilisateur doit etre compose de (Maj,Min,numbers,Caractere Speciale(-_) seulement"
            self.Info_Msg(info_title=info_title,info_text=info_text)
            return
        
        ##Sign In 
        Sign_In_Response = BACKEND.SignIn.Sign_In_Admin(username,password)
        self.Info_Msg(info_title=Sign_In_Response["title"],info_text=Sign_In_Response["text"])

        ##Sign In Failed
        if (Sign_In_Response["type"] == "error"):
            return
        self.close()
        data = {"username":username}
        fp = open("entreprise.pkl","wb")
        pickle.dump(data,fp)
        fp.close()
        os.system(f"Python ./Dashboard.py {username}")

    def Register_To_DB(self):
        username = str(self.username_register.toPlainText())
        password = str(self.password_register.toPlainText())

        if(BACKEND.Validation.Isvalid_Password(password)==None):
            info_title = "Format Error"
            info_text = "Wrong Password Format \nPassword must be at least 8 chars (Uppercase,Lowercase,numbers,specialchars(-@#$%^&+=_) "
            self.Info_Msg(info_title=info_title,info_text=info_text)
            return

        if(BACKEND.Validation.Isvalid_Username(username) == None):
            info_title = "Format Error"
            info_text = "Wrong Username Format \nUsername must be composed of (Uppercase,Lowercase,numbers,specialchars(-_) only "
            self.Info_Msg(info_title=info_title,info_text=info_text)
            return
    
        ##Sign Up 
        Sign_Up_Response = BACKEND.SignUp.Sign_Up_Admin(username,password)
        self.Info_Msg(info_title=Sign_Up_Response["title"],info_text=Sign_Up_Response["text"])

        ##Sign Up  Failed
        if (Sign_Up_Response["type"] == "error"):
            return

                
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    app.exec_()
