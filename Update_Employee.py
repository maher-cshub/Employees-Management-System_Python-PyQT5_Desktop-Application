from PyQt5.QtWidgets import QApplication, QMainWindow,QMessageBox,QDateEdit,QDesktopWidget
from PyQt5.uic import loadUi
from PyQt5.QtCore import QDate
import BACKEND.SignIn, BACKEND.SignUp, BACKEND.Validation, BACKEND.EmployeeManipulate
import sys
import pickle
from datetime import date,datetime,timedelta


MAIN_UI = "./UI"
USER_NAME = ""
EMPLOYEE = {}
TODAY = datetime.today().strftime('%d/%m/%Y')
##MAIN CLASS 

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

def Load_Data():
    global USER_NAME
    global EMPLOYEE
    fp = open("employe_to_update.pkl","rb")
    data = pickle.load(fp)
    USER_NAME = data["username"]
    EMPLOYEE = data["employee"]
    fp.close()

def Check_Form(employee):
    for value in employee.values():
        if(str(value).isspace() or str(value)==''):
            return Info_Msg("Erreur Champ(s) Vide(s)","Veuillez remplir tous le(s) champ(s) vide(s) !!!","erreur")
    if not BACKEND.Validation.Isvalid_Address(employee["addresse"]):
        return Info_Msg("Erreur Addresse Invalid","Veuillez saisir une Addresse valide !!!","erreur")
    if not BACKEND.Validation.Isvalide_NumTel(employee["num_tel"]):
        return Info_Msg("Erreur Num Tel Invalid","Veuillez saisir un Numero De Telephone valide !!!","erreur")
    ##if not(employee["date_fin_travail"] == "EN_TRAVAIL") and (not BACKEND.Validation.Isvalide_DateOfEndWork(employee["date_fin_travail"],employee["date_debut_travail"])):
    ##    return Info_Msg("Erreur Date Fin Travail Invalid","Veuillez saisir une Date Debut Travail valide !!!","erreur")
    if not BACKEND.Validation.Isvalid_Obsrevation(employee["observation"]):
        return Info_Msg("Erreur observation Invalid Invalid","Veuillez saisir une Observation valide !!!","erreur")
    return Info_Msg("Success","Infos Employe Correctes","success")

class Main(QMainWindow):
    def __init__(self):
        super(Main,self).__init__()
        loadUi(f"{MAIN_UI}/update_employee_window.ui",self)
        self.employee_nom_input.setText(EMPLOYEE["nom"])
        self.employee_prenom_input.setText(EMPLOYEE["prenom"])
        self.employee_date_de_naissance_input.setDate(QDate.fromString(EMPLOYEE["date_naissance"],"d/M/yyyy"))
        self.employee_addresse_input.setText(EMPLOYEE["addresse"])
        self.employee_date_debut_travail_input.setDate(QDate.fromString(EMPLOYEE["date_debut_travail"],"d/M/yyyy"))
        ##self.employee_date_fin_travail_input.setDate(QDate.fromString(EMPLOYEE["date_fin_travail"],"d/M/yyyy"))
        self.employee_num_tel_input.setText(EMPLOYEE["num_tel"])
        self.employee_num_carte_nationale_input.setText(EMPLOYEE["num_carte_nationale"])
        self.employee_salaire_input.setValue(int(str(EMPLOYEE["salaire"]).replace(",","")))
        self.employee_observation_input.setText(EMPLOYEE["observation"])
        self.employee_nom_input.setReadOnly(True)
        self.employee_prenom_input.setReadOnly(True)
        self.employee_date_de_naissance_input.setReadOnly(True)
        self.employee_num_carte_nationale_input.setReadOnly(True)
        self.employee_date_debut_travail_input.setReadOnly(True)
        self.update_employee_btn.clicked.connect(self.Update_Employee)

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

    def Update_Employee(self):
        global USER_NAME
        new_employee = EMPLOYEE
        new_employee["num_tel"] = self.employee_num_tel_input.text()
        new_employee["addresse"] = self.employee_addresse_input.text()
        new_employee["salaire"] = self.employee_salaire_input.text()
        new_employee["date_debut_travail"] = self.employee_date_debut_travail_input.text()
        new_employee["date_fin_travail"] = "EN_TRAVAIL" if self.en_travail.isChecked() else str(TODAY) ##self.employee_date_debut_travail_input.text() ##self.employee_date_fin_travail_input.date().toPyDate().strftime('%d/%m/%Y')
        new_employee["observation"] = self.employee_observation_input.toPlainText()
        validation_response = Check_Form(new_employee)
        self.Info_Msg_Show(validation_response["title"],validation_response["content"])
        if(validation_response["type"] == "success"):
            response = BACKEND.EmployeeManipulate.Update_Employee(USER_NAME,new_employee,EMPLOYEE["num_carte_nationale"])
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

