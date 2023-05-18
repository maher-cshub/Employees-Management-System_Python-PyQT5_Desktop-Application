from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidgetItem,QMessageBox,QDesktopWidget
from PyQt5.uic import loadUi
from PyQt5 import QtCore,QtWidgets
import BACKEND.SignIn, BACKEND.SignUp, BACKEND.Validation,BACKEND.PresenceManipulate,BACKEND.PayementsManipulate
import sys
import pickle


MAIN_UI = "./UI"
USER_NAME = ''
PRESENCE = None
##MAIN CLASS 

def Load_User():
    global USER_NAME
    fp = open("entreprise.pkl","rb")
    data = pickle.load(fp)
    USER_NAME = data["username"]
    fp.close()


def Load_Data():
    global USER_NAME
    global PRESENCE
    fp = open("presence_to_do.pkl","rb")
    data = pickle.load(fp)
    ##print(data)
    USER_NAME = data["username"]
    PRESENCE = data["presence"]
    fp.close()

def Info_Msg(title,content,type):
   info_msg={}
   info_msg["title"] = title 
   info_msg["content"] = content
   info_msg["type"] = type
   return info_msg

class Main(QMainWindow):
    def getTotalTravail(total_travail):
        if (PRESENCE["total_travail"] == '1.0'):
            return "Journee Complete"
        if (PRESENCE["total_travail"] == '0.5'): 
            return "Demi Journee"
        else:
            return "Rien"

    def __init__(self):
        super(Main,self).__init__()
        loadUi(f"{MAIN_UI}/faire_presence_window.ui",self)
        self.num_carte_nationale.setText(PRESENCE["num_employe"])
        self.nom_employe.setText(PRESENCE["nom_employe"])
        self.prenom_employe.setText(PRESENCE["prenom_employe"])
        self.presence_valide.setText(PRESENCE["presence_valide"])
        self.present.setText(PRESENCE["present"])
        self.total_travail.setText(self.getTotalTravail())
        self.num_carte_nationale.setReadOnly(True)
        self.nom_employe.setReadOnly(True)
        self.prenom_employe.setReadOnly(True)
        self.presence_valide.setReadOnly(True)
        self.present.setReadOnly(True)
        self.total_travail.setReadOnly(True)
        self.valider_presence_btn.clicked.connect(self.Valider_Presence)

    '''
        desktop = QDesktopWidget().availableGeometry() # get the available desktop size
        taskbar_height = QDesktopWidget().screenGeometry().height() - QDesktopWidget().availableGeometry().height()
        self.setFixedSize(desktop.width(),desktop.height() - taskbar_height)
        
        frame = self.frameGeometry()
        cp = QDesktopWidget().screenGeometry().center()
        cp.setY(cp.y()-taskbar_height)
        frame.moveCenter(cp)
        

        self.move(frame.topRight())
    '''
        

    def Info_Msg_Show(self,info_title,info_text):
        msgBox1 = QMessageBox()
        msgBox1.setIcon(QMessageBox.Information)
        msgBox1.setWindowTitle(info_title)
        msgBox1.setText(info_text)
        msgBox1.setStandardButtons(QMessageBox.Ok)
        msgBox1.exec()
        return

    def Valider_Presence(self):
        PRESENCE = {}
        presence = "OUI" if self.presence_oui.isChecked() else "NON"
        total_travail = 1.0 if (self.travail_journee_complete.isChecked() and presence == "OUI")  else 0.5 if (self.travail_demi_journee.isChecked() and presence == "OUI") else 0.0
        ##BACKEND
        PRESENCE["NUM_EMPLOYE"] = self.num_carte_nationale.toPlainText()
        PRESENCE["PRESENCE"] = presence
        PRESENCE["TOTAL_TRAVAIL"] = total_travail
        response = BACKEND.PresenceManipulate.Update_Presence(USER_NAME,PRESENCE)
        ##set presence to valid in payement_en_cours
        self.Info_Msg_Show(response["title"],response["content"])
        if(response["type"] == "success"):
            sys.exit(0)
            ##Ajout au DB
        else:
            sys.exit(1)

if __name__ == '__main__':
    Load_User()
    Load_Data()
    app = QApplication(sys.argv)
    window = Main()
    window.showMaximized()
    app.exec_()
