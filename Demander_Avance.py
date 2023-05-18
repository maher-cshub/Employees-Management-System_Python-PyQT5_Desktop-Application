from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidgetItem,QMessageBox,QDesktopWidget
from PyQt5.uic import loadUi
from PyQt5 import QtCore,QtWidgets
import BACKEND.SignIn, BACKEND.SignUp, BACKEND.Validation,BACKEND.PayementsManipulate
import sys
import pickle


MAIN_UI = "./UI"
USER_NAME = ''
AVANCE = None
##MAIN CLASS 

def Load_Data():
    global USER_NAME
    global AVANCE
    fp = open("avance_to_do.pkl","rb")
    data = pickle.load(fp)
    ##print(data)
    USER_NAME = data["username"]
    AVANCE = data["avance"]
    fp.close()

def Info_Msg(title,content,type):
   info_msg={}
   info_msg["title"] = title 
   info_msg["content"] = content
   info_msg["type"] = type
   return info_msg

class Main(QMainWindow):

    def Credit(self):
        new_salaire = int(float(self.salaire.toPlainText().replace(",",""))) - int(float(self.avance.toPlainText()))
        max_a_avancer = None
        self.somme_a_avancer.setMaximum(new_salaire)
        max_a_avancer = new_salaire
        return max_a_avancer

    def NoCredit(self):
        total_a_payer = float(self.total_a_payer.toPlainText().replace(",",""))
        max_a_avancer = None
        if(total_a_payer<= 0):
            self.somme_a_avancer.setMaximum(0)
            max_a_avancer = 0
        else:
            self.somme_a_avancer.setMaximum(int(total_a_payer))
            max_a_avancer = int(total_a_payer)
        return max_a_avancer

    def __init__(self):
        super(Main,self).__init__()
        loadUi(f"{MAIN_UI}/faire_avance_window.ui",self)
        self.num_carte_nationale.setText(AVANCE["num_employe"])
        self.nom_employe.setText(AVANCE["nom_employe"])
        self.prenom_employe.setText(AVANCE["prenom_employe"])
        self.salaire.setText(AVANCE["salaire"])
        self.avance.setText(AVANCE["avance"])
        self.total_a_payer.setText(AVANCE["total_a_payer"])
        self.num_carte_nationale.setReadOnly(True)
        self.nom_employe.setReadOnly(True)
        self.prenom_employe.setReadOnly(True)
        self.salaire.setReadOnly(True)
        self.avance.setReadOnly(True)
        self.total_a_payer.setReadOnly(True)
        self.somme_a_avancer.setMaximum(self.Credit() if self.credit_oui.isChecked() else self.NoCredit())
        self.somme_a_avancer.setValue(0)
        self.credit_oui.toggled.connect(self.Credit)
        self.credit_non.toggled.connect(self.NoCredit)
        self.valider_avance_btn.clicked.connect(self.Valider_Avance)


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

    def Valider_Avance(self):
        NOUVELLE_AVANCE = {}
        NOUVELLE_AVANCE["NUM_EMPLOYE"] = AVANCE["num_employe"]
        NOUVELLE_AVANCE["ENTREPRISE_DU_TRAVAIL"] = USER_NAME
        NOUVELLE_AVANCE["SALAIRE"] = AVANCE["salaire"]
        NOUVELLE_AVANCE["AVANCE"] = str(int(float(AVANCE["avance"])) + int(self.somme_a_avancer.value()))
        NOUVELLE_AVANCE["TOTAL_A_PAYER"] = AVANCE["total_a_payer"]
        NOUVELLE_AVANCE["TOTAL_JOURS_TRAVAIL"] = AVANCE["total_jours_travail"]
        response = BACKEND.PayementsManipulate.UpdateAvanceInCurrentPayement(NOUVELLE_AVANCE)
        self.Info_Msg_Show(response["title"],response["content"])
        if(response["type"] == "success"):
            sys.exit(0)
            ##Ajout au DB
        else:
            sys.exit(1)

if __name__ == '__main__':
    Load_Data()
    app = QApplication(sys.argv)
    window = Main()
    window.showMaximized()
    app.exec_()
    