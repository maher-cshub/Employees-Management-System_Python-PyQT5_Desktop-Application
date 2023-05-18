from PyQt5.QtWidgets import QApplication, QMainWindow,QMessageBox,QDesktopWidget
from PyQt5.uic import loadUi
import BACKEND.SignIn, BACKEND.SignUp, BACKEND.Validation, BACKEND.EmployeeManipulate, BACKEND.PayementsManipulate,BACKEND.PresenceManipulate
from datetime import date,datetime,timedelta
import sys
import pickle

MAIN_UI = "./UI"
USER_NAME = sys.argv[1]
TODAY = datetime.today().strftime('%d/%m/%Y')

def Info_Msg(title,content,type):
   info_msg={}
   info_msg["title"] = title 
   info_msg["content"] = content
   info_msg["type"] = type
   return info_msg

def Load_User():
    global USER_NAME
    fp = open("entreprise.pkl","rb")
    data = pickle.load(fp)
    USER_NAME = data["username"]
    fp.close()

def Check_Form(employee):
    for value in employee.values():
        if(str(value).isspace() or str(value)==''):
            return Info_Msg("Erreur Champ(s) Vide(s)","Veuillez remplir tous le(s) champ(s) vide(s) !!!","erreur")
    if not BACKEND.Validation.Isvalid_Name(employee["nom"]):
        return Info_Msg("Erreur Nom Invalid","Veuillez saisir un nom valide !!!","erreur")
    if not BACKEND.Validation.Isvalid_Name(employee["prenom"]):
        return Info_Msg("Erreur Prenom Invalid","Veuillez saisir un prenom valide !!!","erreur")
    if not BACKEND.Validation.Isvalide_NumTel(employee["num_tel"]):
        return Info_Msg("Erreur Num Tel Invalid","Veuillez saisir un numero de telephone valide !!!","erreur")
    if not BACKEND.Validation.Isvalide_DateOfBirth(employee["date_naissance"]):
        return Info_Msg("Erreur Date Naissance Invalid","Veuillez saisir un Date de Naissance valide !!!","erreur")
    if not BACKEND.Validation.Isvalid_Address(employee["addresse"]):
        return Info_Msg("Erreur Addresse Invalid","Veuillez saisir une Addresse valide !!!","erreur")
    if not BACKEND.Validation.Isvalid_NumCarteNationale(employee["num_carte_nationale"]):
        return Info_Msg("Erreur Num Carte Nationale Invalid","Veuillez saisir un Num de Carte Nationale valide !!!","erreur")
    if not BACKEND.Validation.Isvalide_DateOfStartWork(employee["date_debut_travail"],employee["date_naissance"]):
        return Info_Msg("Erreur Date Debut Travail Invalid","Veuillez saisir une Date Debut Travail valide !!!","erreur")
    if not BACKEND.Validation.Isvalid_Obsrevation(employee["observation"]):
        return Info_Msg("Erreur observation Invalid Invalid","Veuillez saisir une Observation valide !!!","erreur")
    return Info_Msg("Ajout avec Succes","Employee Ajoutee avec Succes","success")

class Main(QMainWindow):
    def __init__(self):
        super(Main,self).__init__()
        loadUi(f"{MAIN_UI}/add_employee_window.ui",self)
        self.add_employee_btn.clicked.connect(self.Add_Employee)

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

    def Add_Employee(self):
        employee = {}
        employee["nom"] = self.employee_nom_input.text()
        employee["prenom"] = self.employee_prenom_input.text()
        employee["num_tel"] = self.employee_num_tel_input.text()
        employee["entreprise_de_travail"] = USER_NAME
        employee["date_naissance"] = self.employee_date_de_naissance_input.date().toPyDate().strftime('%d/%m/%Y')
        employee["addresse"] = self.employee_addresse_input.text()
        employee["num_carte_nationale"] = self.employee_num_carte_nationale_input.text()
        employee["salaire"] = self.employee_salaire_input.text()
        employee["date_debut_travail"] = str(TODAY)
        employee["date_fin_travail"] = "EN_TRAVAIL"
        employee["observation"] = self.employee_observation_input.toPlainText()

        validation_response = Check_Form(employee)
        
        self.Info_Msg_Show(validation_response["title"],validation_response["content"])

        if(validation_response["type"] == "success"):
            response = BACKEND.EmployeeManipulate.Add_Employee(employee)
            if(response["type"] == "success"):

                ##ADD payments stats
                BACKEND.PayementsManipulate.SetDefaultPayement(employee)
                BACKEND.PresenceManipulate.Set_Presence(employee)
                sys.exit(0)
                ##Ajout au DB
            else:
                self.Info_Msg_Show(response["title"],response["content"])
                sys.exit(1)

if __name__ == '__main__':
    Load_User()
    app = QApplication(sys.argv)
    window = Main()
    window.showMaximized()
    app.exec_()

