from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidgetItem,QMessageBox,QDesktopWidget,QFileDialog,QPushButton
from PyQt5.uic import loadUi
from PyQt5 import QtCore,QtWidgets
import BACKEND.SignIn, BACKEND.SignUp, BACKEND.Validation, BACKEND.EmployeeManipulate,BACKEND.PayementsManipulate,BACKEND.PresenceManipulate
import sys
import os
import pickle
import time
from datetime import date,datetime,timedelta
import pandas as pd

MAIN_UI = "./UI"
USER_NAME = ""
DATA_BASE = "./BACKEND/data"
LISTE_EMPLOYES = []
LISTE_PRESENCE = []
PAYEMENTS_EN_COURS = []
PAYEMENTS_A_FAIRE = []
PAYEMENTS_REUSSIS = []
PAYEMENTS_REUSSIS_FILTERED = []
CREDITS = []
TODAY = datetime.today().strftime('%d/%m/%Y')
CURRENT_TIME = datetime.now()


def Load_User():
    global USER_NAME
    fp = open("entreprise.pkl","rb")
    data = pickle.load(fp)
    USER_NAME = data["username"]
    fp.close()

##MAIN CLASS 
class Main(QMainWindow):

    def Info_Msg(self,info_title,info_text):
        msgBox1 = QMessageBox()
        msgBox1.setIcon(QMessageBox.Information)
        msgBox1.setWindowTitle(info_title)
        msgBox1.setText(info_text)
        msgBox1.setStandardButtons(QMessageBox.Ok)
        msgBox1.exec()
        return
    
    def Set_Today(self):
        self.today_label.setText(f"Aujourd'hui Le: {TODAY}")
        ##print(CURRENT_TIME.hour)
        if (CURRENT_TIME.hour >= 00 and  CURRENT_TIME.hour <= 12 ):
            self.organisation_name.setText(f"Bonjour   {USER_NAME}")
        else:
            self.organisation_name.setText(f"Bonsoir   {USER_NAME}")


    def Load_Data(self):
        self.Show_Employees()
        self.Show_Presence()
        self.Show_Payements_En_Cours()
        self.Show_Payements_A_Faire()
        self.Show_Credits()
        self.Show_Payements_Reussi()


    def Sync_Date(self):
        self.Set_Today()
        BACKEND.PayementsManipulate.CheckCurrentPayements(USER_NAME)
        results = BACKEND.PresenceManipulate.Sync_Presence(USER_NAME)
        if (len(results) != 0):
            BACKEND.PayementsManipulate.UpdatePresenceInCurrentPayement(results)
            BACKEND.PayementsManipulate.UpdateNextPayementDateInCurrentPayement(USER_NAME)
        BACKEND.PayementsManipulate.UpdateRetardPayemenetInPendingPayement(USER_NAME)
        self.Load_Data()
        return 

    def __init__(self):

        super(Main,self).__init__()
        loadUi(f"{MAIN_UI}/dashboard_window.ui",self)

        # main thread is carrying on..
        
        ##pages navigation
        self.liste_employee_btn.clicked.connect(lambda : self.stackedWidget.setCurrentWidget(self.liste_employees_page))
        self.liste_presence_btn.clicked.connect(lambda : self.stackedWidget.setCurrentWidget(self.liste_presence_page))
        self.payements_en_cours_btn.clicked.connect(lambda : self.stackedWidget.setCurrentWidget(self.payements_en_cours_page))
        self.payements_a_faire_btn.clicked.connect(lambda : self.stackedWidget.setCurrentWidget(self.payements_a_faire_page))
        self.payements_reussis_btn.clicked.connect(lambda : self.stackedWidget.setCurrentWidget(self.payements_reussis_page))
        self.credits_btn.clicked.connect(lambda : self.stackedWidget.setCurrentWidget(self.credit_page))

        for button in self.SideBar_Frame_Buttons.findChildren(QPushButton):
            button.clicked.connect(self.Apply_Style)


        ##liste employes buttons
        self.add_employee_btn.clicked.connect(self.Add_Employee_Window)
        self.update_employee_btn.clicked.connect(self.Update_Employe_Window)
        self.delete_employee_btn.clicked.connect(self.Delete_Employe)
        self.liste_employee_search_btn.clicked.connect(self.Search_Liste_Employee)
        ##self.liste_employee_filter_btn.clicked.connect(self.Filter_Liste_Employee)

        ##liste presence buttons
        self.faire_presence_btn.clicked.connect(self.Faire_Presence)
        self.liste_presence_search_btn.clicked.connect(self.Search_Liste_Presence)
        ##self.faire_presence_filter_btn.clicked.connect(self.Search_Liste_Presence)

        ##payements en cours buttons
        self.demander_avance_btn.clicked.connect(self.Demander_Avance)
        self.payements_en_cours_search_btn.clicked.connect(self.Search_Payement_En_Cours)
        ##self.payements_en_cours_filter_btn.clicked.connect(self.Filter_Payement_En_Cours)


        ##payements a faire buttons
        self.payer_payement_a_faire_btn.clicked.connect(self.Payer_Payement_A_Faire)
        self.payements_a_faire_search_btn.clicked.connect(self.Search_Payement_A_Faire)
        ##self.payements_a_faire_filter_btn.clicked.connect(self.Filter_Payement_A_Faire)

        ##payement reussi buttons
        self.export_payements_reussis_btn.clicked.connect(self.Export_Payements_Reussi)
        self.payements_reussis_search_btn.clicked.connect(self.Search_Payement_Reussis)
        ##self.payements_reussis_filter_btn.clicked.connect(self.Filter_Payement_Reussis)


        ##credit buttons
        self.payer_credit_btn.clicked.connect(self.Payer_Credit)
        self.credit_recherche_btn.clicked.connect(self.Search_Credit)
        ##self.credit_filter_btn.clicked.connect(self.Filter_Credit)

        ##sync date btn
        self.sync_date_btn.clicked.connect(self.Sync_Date)

        self.contact_btn.clicked.connect(self.Contact)
        
        self.Set_Today()
        self.Load_Data()
        self.Sync_Date()

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

    def Apply_Style(self):
        for button in self.SideBar_Frame_Buttons.findChildren(QPushButton):
            if (button.objectName() != self.sender().objectName()):
                style = button.styleSheet().replace("background-color:rgb(255, 234, 8);","background-color: rgb(25, 25, 25);").replace("color:rgb(0,0,0);","color: rgb(255, 255, 255);").replace("border-left: 3px solid rgb(255, 234, 8);","border-left: 3px solid rgb(25, 25, 25);")
                button.setStyleSheet(style)
            new_style = self.sender().styleSheet().replace("background-color: rgb(25, 25, 25);","background-color:rgb(255, 234, 8);").replace("color: rgb(255, 255, 255);","color:rgb(0,0,0);").replace("border-left: 3px solid rgb(25, 25, 25);","border-left: 3px solid rgb(255, 234, 8);")
            self.sender().setStyleSheet(new_style)

        


    def Contact(self):
        stat = os.system(f"Python ./contact.py {USER_NAME}")

    def Add_Employee_Window(self):
        stat = os.system(f"Python ./Add_Employee.py {USER_NAME}")
        self.Load_Data()

    def Update_Employe_Window(self):
        indexes = self.liste_employee_table.selectionModel().selectedRows()
        if(len(indexes) != 1):
            self.Info_Msg("Erreur","Veuillez selection un seul employe a modifier dans la liste de employes !")
            return
        index = indexes[0]
        employee = {}
        employee["nom"] = self.liste_employee_table.item(index.row(), 0).text()
        employee["prenom"] = self.liste_employee_table.item(index.row(), 1).text()
        employee["num_tel"] = self.liste_employee_table.item(index.row(), 2).text()
        employee["date_naissance"] = self.liste_employee_table.item(index.row(), 3).text()
        employee["addresse"] = self.liste_employee_table.item(index.row(), 4).text()
        employee["num_carte_nationale"] = self.liste_employee_table.item(index.row(), 5).text()
        employee["date_debut_travail"] = self.liste_employee_table.item(index.row(), 6).text()
        employee["date_fin_travail"] = self.liste_employee_table.item(index.row(), 7).text()
        employee["salaire"] = self.liste_employee_table.item(index.row(), 8).text()
        employee["observation"] = self.liste_employee_table.item(index.row(), 9).text()
        data = {"username":USER_NAME,"employee":employee}
        fp = open("employe_to_update.pkl","wb")
        pickle.dump(data,fp)
        fp.close()
        stat = os.system(f"Python ./Update_Employee.py")
        self.Load_Data()

    def Delete_Employe(self):
        indexes = self.liste_employee_table.selectionModel().selectedRows()
        if(len(indexes) == 0):
            self.Info_Msg("Erreur","Veuillez selection l'(es) employe(s) a supprimer dans la liste de employes !")
            return
        employees_ids = [] 
        for index in sorted(indexes):
            employees_ids.append(self.liste_employee_table.item(index.row(), 5).text())
        employees_ids = ",".join([str(employee) for employee in employees_ids])
        response = BACKEND.EmployeeManipulate.Delete_Employe(USER_NAME,employees_ids)
        self.Info_Msg(response["title"],response["content"])
        self.Load_Data()

    def Show_Employees(self):
        global LISTE_EMPLOYES
        self.liste_employee_table.setRowCount(0)
        LISTE_EMPLOYES = BACKEND.EmployeeManipulate.Show_Employees(USER_NAME)
        total_rows = len(LISTE_EMPLOYES)
        total_colums = self.liste_employee_table.columnCount()
        self.liste_employee_table.setColumnCount(total_colums)
        for row in range(total_rows):
            self.liste_employee_table.insertRow(row) 
            for column in range(total_colums):
                item = QtWidgets.QTableWidgetItem(str(list(LISTE_EMPLOYES[row])[column]))
                item.setFlags(item.flags() ^ QtCore.Qt.ItemIsEditable)
                self.liste_employee_table.setItem(row, column, item)

    def Show_Presence(self):
        global LISTE_PRESENCE
        self.liste_presence_table.setRowCount(0)
        LISTE_PRESENCE = BACKEND.PresenceManipulate.Show_Presence(USER_NAME)
        total_rows = len(LISTE_PRESENCE)
        total_colums = self.liste_presence_table.columnCount()
        self.liste_presence_table.setColumnCount(total_colums)
        for row in range(total_rows):
            self.liste_presence_table.insertRow(row) 
            for column in range(total_colums):
                item = QtWidgets.QTableWidgetItem(str(list(LISTE_PRESENCE[row])[column]))
                item.setFlags(item.flags() ^ QtCore.Qt.ItemIsEditable)
                self.liste_presence_table.setItem(row, column, item)

    def Show_Payements_En_Cours(self):
        global PAYEMENTS_EN_COURS
        self.payements_en_cours_table.setRowCount(0)
        PAYEMENTS_EN_COURS = BACKEND.PayementsManipulate.Show_Payements_En_Cours(USER_NAME)
        total_rows = len(PAYEMENTS_EN_COURS)
        total_colums = self.payements_en_cours_table.columnCount()
        self.payements_en_cours_table.setColumnCount(total_colums)
        for row in range(total_rows):
            self.payements_en_cours_table.insertRow(row) 
            for column in range(total_colums):
                item = QtWidgets.QTableWidgetItem(str(list(PAYEMENTS_EN_COURS[row])[column]))
                item.setFlags(item.flags() ^ QtCore.Qt.ItemIsEditable)
                self.payements_en_cours_table.setItem(row, column, item)

    def Faire_Presence(self):
        indexes = self.liste_presence_table.selectionModel().selectedRows()
        if(len(indexes) != 1):
            self.Info_Msg("Erreur","Veuillez selectionnez un seul employe pour faire se presnece !")
            return
        index = indexes[0]
        presence = {}
        presence["num_employe"] = self.liste_presence_table.item(index.row(), 0).text()
        presence["nom_employe"] = self.liste_presence_table.item(index.row(), 1).text()
        presence["prenom_employe"] = self.liste_presence_table.item(index.row(), 2).text()
        presence["presence_valide"] = self.liste_presence_table.item(index.row(), 3).text()
        presence["present"] = self.liste_presence_table.item(index.row(), 4).text()
        presence["total_travail"] = self.liste_presence_table.item(index.row(), 5).text()
        data = {"username":USER_NAME,"presence":presence}
        fp = open("presence_to_do.pkl","wb")
        pickle.dump(data,fp)
        fp.close()
        stat = os.system(f"Python ./Faire_Presence.py")
        self.Load_Data()

    def Demander_Avance(self):
        indexes = self.payements_en_cours_table.selectionModel().selectedRows()
        if(len(indexes) != 1):
            self.Info_Msg("Erreur","Veuillez selectionnez un seul employe pour demander l'avance !")
            return
        index = indexes[0]
        avance = {}
        avance["num_employe"] = self.payements_en_cours_table.item(index.row(), 0).text()
        avance["nom_employe"] = self.payements_en_cours_table.item(index.row(), 1).text()
        avance["prenom_employe"] = self.payements_en_cours_table.item(index.row(), 2).text()
        avance["total_jours_travail"] = self.payements_en_cours_table.item(index.row(),5).text()
        avance["salaire"] = self.payements_en_cours_table.item(index.row(), 6).text()
        avance["avance"] = self.payements_en_cours_table.item(index.row(), 7).text()
        avance["total_a_payer"] = self.payements_en_cours_table.item(index.row(), 8).text()
        data = {"username":USER_NAME,"avance":avance}
        fp = open("avance_to_do.pkl","wb")
        pickle.dump(data,fp)
        fp.close()
        stat = os.system(f"Python ./Demander_Avance.py")
        self.Load_Data()
        return

    def Payer_Credit(self):
        indexes = self.credit_table.selectionModel().selectedRows()
        if(len(indexes) != 1):
            self.Info_Msg("Erreur","Veuillez selectionnez un seul employe pour faire se presnece !")
            return
        index = indexes[0]
        credit = {}
        credit["num_employe"] = int(self.credit_table.item(index.row(), 0).text())
        credit["date_credits"] = self.credit_table.item(index.row(), 5).text()
        BACKEND.PayementsManipulate.DeleteCredit(USER_NAME,credit)
        self.Load_Data()

    def Show_Payements_A_Faire(self):
        global PAYEMENTS_A_FAIRE
        self.payements_a_faire_table.setRowCount(0)
        PAYEMENTS_A_FAIRE = BACKEND.PayementsManipulate.Show_Payements_A_Faire(USER_NAME)
        total_rows = len(PAYEMENTS_A_FAIRE)
        total_colums = self.payements_a_faire_table.columnCount()
        self.payements_a_faire_table.setColumnCount(total_colums)
        for row in range(total_rows):
            self.payements_a_faire_table.insertRow(row) 
            for column in range(total_colums):
                item = QtWidgets.QTableWidgetItem(str(list(PAYEMENTS_A_FAIRE[row])[column]))
                item.setFlags(item.flags() ^ QtCore.Qt.ItemIsEditable)
                self.payements_a_faire_table.setItem(row, column, item)
        return

    def Show_Credits(self):
        global CREDITS
        self.credit_table.setRowCount(0)
        CREDITS = BACKEND.PayementsManipulate.Show_Credits(USER_NAME)
        total_rows = len(CREDITS)
        total_colums = self.credit_table.columnCount()
        self.credit_table.setColumnCount(total_colums)
        for row in range(total_rows):
            self.credit_table.insertRow(row) 
            for column in range(total_colums):
                item = QtWidgets.QTableWidgetItem(str(list(CREDITS[row])[column]))
                item.setFlags(item.flags() ^ QtCore.Qt.ItemIsEditable)
                self.credit_table.setItem(row, column, item)   
        return
    
    def Show_Payements_Reussi(self):
        global PAYEMENTS_REUSSIS
        global PAYEMENTS_REUSSIS_FILTERED
        self.payements_reussis_table.setRowCount(0)
        PAYEMENTS_REUSSIS = BACKEND.PayementsManipulate.Show_Payements_Reussis(USER_NAME)
        PAYEMENTS_REUSSIS_FILTERED = PAYEMENTS_REUSSIS
        total_rows = len(PAYEMENTS_REUSSIS)
        total_colums = self.payements_reussis_table.columnCount()
        self.payements_reussis_table.setColumnCount(total_colums)
        for row in range(total_rows):
            self.payements_reussis_table.insertRow(row) 
            for column in range(total_colums):
                item = QtWidgets.QTableWidgetItem(str(list(PAYEMENTS_REUSSIS[row])[column]))
                item.setFlags(item.flags() ^ QtCore.Qt.ItemIsEditable)
                self.payements_reussis_table.setItem(row, column, item)   
        return

    def Show_Searched_Employees(self,liste):
        self.liste_employee_table.setRowCount(0)
        total_rows = len(liste)
        total_colums = self.liste_employee_table.columnCount()
        self.liste_employee_table.setColumnCount(total_colums)
        for row in range(total_rows):
            self.liste_employee_table.insertRow(row) 
            for column in range(total_colums):
                item = QtWidgets.QTableWidgetItem(str(list(liste[row])[column]))
                item.setFlags(item.flags() ^ QtCore.Qt.ItemIsEditable)
                self.liste_employee_table.setItem(row, column, item)
            
    def Show_Searched_Presences(self,liste):
        self.liste_presence_table.setRowCount(0)
        total_rows = len(liste)
        total_colums = self.liste_presence_table.columnCount()
        self.liste_presence_table.setColumnCount(total_colums)
        for row in range(total_rows):
            self.liste_presence_table.insertRow(row) 
            for column in range(total_colums):
                item = QtWidgets.QTableWidgetItem(str(list(liste[row])[column]))
                item.setFlags(item.flags() ^ QtCore.Qt.ItemIsEditable)
                self.liste_presence_table.setItem(row, column, item)


    def Show_Searched_Payements_En_Cours(self,liste):
        self.payements_en_cours_table.setRowCount(0)
        total_rows = len(liste)
        total_colums = self.payements_en_cours_table.columnCount()
        self.payements_en_cours_table.setColumnCount(total_colums)
        for row in range(total_rows):
            self.payements_en_cours_table.insertRow(row) 
            for column in range(total_colums):
                item = QtWidgets.QTableWidgetItem(str(list(liste[row])[column]))
                item.setFlags(item.flags() ^ QtCore.Qt.ItemIsEditable)
                self.payements_en_cours_table.setItem(row, column, item)


    def Show_Searched_Payements_A_Faire(self,liste):
        self.payements_a_faire_table.setRowCount(0)
        total_rows = len(liste)
        total_colums = self.payements_a_faire_table.columnCount()
        self.payements_a_faire_table.setColumnCount(total_colums)
        for row in range(total_rows):
            self.payements_a_faire_table.insertRow(row) 
            for column in range(total_colums):
                item = QtWidgets.QTableWidgetItem(str(list(liste[row])[column]))
                item.setFlags(item.flags() ^ QtCore.Qt.ItemIsEditable)
                self.payements_a_faire_table.setItem(row, column, item)


    def Show_Searched_Payements_Reussis(self,liste):
        self.payements_reussis_table.setRowCount(0)
        total_rows = len(liste)
        total_colums = self.payements_reussis_table.columnCount()
        self.payements_reussis_table.setColumnCount(total_colums)
        for row in range(total_rows):
            self.payements_reussis_table.insertRow(row) 
            for column in range(total_colums):
                item = QtWidgets.QTableWidgetItem(str(list(liste[row])[column]))
                item.setFlags(item.flags() ^ QtCore.Qt.ItemIsEditable)
                self.payements_reussis_table.setItem(row, column, item)


    def Show_Searched_Credits(self,liste):
        self.credit_table.setRowCount(0)
        total_rows = len(liste)
        total_colums = self.credit_table.columnCount()
        self.credit_table.setColumnCount(total_colums)
        for row in range(total_rows):
            self.credit_table.insertRow(row) 
            for column in range(total_colums):
                item = QtWidgets.QTableWidgetItem(str(list(liste[row])[column]))
                item.setFlags(item.flags() ^ QtCore.Qt.ItemIsEditable)
                self.credit_table.setItem(row, column, item)
    
    
    def Search_Liste_Employee(self):
        global LISTE_EMPLOYES
        if (str(self.liste_employee_search_field.text()).isspace() or str(self.liste_employee_search_field.text()) == ""):
            self.Show_Searched_Employees(LISTE_EMPLOYES)
            return
        else:
            if(str(self.liste_employee_search_field.text()).isnumeric()):
                ##check for carte national
                num_carte = self.liste_employee_search_field.text()
                if(BACKEND.Validation.Isvalid_NumCarteNationale(num_carte)):
                    liste_employees = [elt for elt in LISTE_EMPLOYES if elt[5] == num_carte]
                    self.Show_Searched_Employees(liste_employees)
                    return
                else:
                    self.Info_Msg("Erreur","invalid input (Veuillez Entrer un numero de carte valide)")
                    return
            if (str(self.liste_employee_search_field.text()).isalpha()):
                ##check for name and prenom
                nom_or_prenom = str.lower(self.liste_employee_search_field.text())
                if (BACKEND.Validation.Isvalid_Name(nom_or_prenom)):
                    liste_employees = [elt for elt in LISTE_EMPLOYES if (str.lower(elt[0]) == nom_or_prenom or str.lower(elt[1]) == nom_or_prenom)]
                    self.Show_Searched_Employees(liste_employees)
                    return
                else:
                    self.Info_Msg("Erreur","invalid input (Veuillez Entrer un (nom ou prenom) valide)")
                    return
            else:
                self.Info_Msg("Erreur","invalid input (Veuillez Entrer (un nom ou un prenom ou numero de carte nationale) valide)")
                return



    def Search_Liste_Presence(self):
        global LISTE_PRESENCE
        if (str(self.liste_presence_search_field.text()).isspace() or str(self.liste_presence_search_field.text()) == ""):
            self.Show_Searched_Presences(LISTE_PRESENCE)
            return
        else:
            if(str(self.liste_presence_search_field.text()).isnumeric()):
                ##check for carte national
                num_carte = self.liste_presence_search_field.text()
                if(BACKEND.Validation.Isvalid_NumCarteNationale(num_carte)):
                    liste_presence = [elt for elt in LISTE_PRESENCE if str(elt[0]) == num_carte]
                    self.Show_Searched_Presences(liste_presence)
                    return
                else:
                    self.Info_Msg("Erreur","invalid input (Veuillez Entrer un numero de carte valide)")
                    return
            if (str(self.liste_presence_search_field.text()).isalpha()):
                ##check for name and prenom
                nom_or_prenom = str.lower(self.liste_presence_search_field.text())
                if (BACKEND.Validation.Isvalid_Name(nom_or_prenom)):
                    liste_presence = [elt for elt in LISTE_PRESENCE if (str.lower(elt[1]) == nom_or_prenom or str.lower(elt[2]) == nom_or_prenom)]
                    self.Show_Searched_Presences(liste_presence)
                    return
                else:
                    self.Info_Msg("Erreur","invalid input (Veuillez Entrer un (nom ou prenom) valide)")
                    return
            else:
                self.Info_Msg("Erreur","invalid input (Veuillez Entrer (un nom ou un prenom ou numero de carte nationale) valide)")
                return


    def Search_Payement_En_Cours(self):
        global PAYEMENTS_EN_COURS
        if (str(self.payements_en_cours_search_field.text()).isspace() or str(self.payements_en_cours_search_field.text()) == ""):
            self.Show_Searched_Payements_En_Cours(PAYEMENTS_EN_COURS)
            return
        else:
            if(str(self.payements_en_cours_search_field.text()).isnumeric()):
                ##check for carte national
                num_carte = self.payements_en_cours_search_field.text()
                if(BACKEND.Validation.Isvalid_NumCarteNationale(num_carte)):
                    liste_payements = [elt for elt in PAYEMENTS_EN_COURS if elt[0] == num_carte]
                    self.Show_Searched_Payements_En_Cours(liste_payements)
                    return
                else:
                    self.Info_Msg("Erreur","invalid input (Veuillez Entrer un numero de carte valide)")
                    return
            if (str(self.payements_en_cours_search_field.text()).isalpha()):
                ##check for name and prenom
                nom_or_prenom = str.lower(self.payements_en_cours_search_field.text())
                if (BACKEND.Validation.Isvalid_Name(nom_or_prenom)):
                    liste_payements = [elt for elt in PAYEMENTS_EN_COURS if (str.lower(elt[1]) == nom_or_prenom or str.lower(elt[2]) == nom_or_prenom)]
                    self.Show_Searched_Payements_En_Cours(liste_payements)
                    return
                else:
                    self.Info_Msg("Erreur","invalid input (Veuillez Entrer un (nom ou prenom) valide)")
                    return
            else:
                self.Info_Msg("Erreur","invalid input (Veuillez Entrer (un nom ou un prenom ou numero de carte nationale) valide)")
                return

    def Search_Payement_A_Faire(self):
        global PAYEMENTS_A_FAIRE
        if (str(self.payements_a_faire_search_field.text()).isspace() or str(self.payements_a_faire_search_field.text()) == ""):
            self.Show_Searched_Payements_A_Faire(PAYEMENTS_A_FAIRE)
            return
        else:
            if(str(self.payements_a_faire_search_field.text()).isnumeric()):
                ##check for carte national
                num_carte = self.payements_a_faire_search_field.text()
                if(BACKEND.Validation.Isvalid_NumCarteNationale(num_carte)):
                    liste_payements = [elt for elt in PAYEMENTS_A_FAIRE if str(elt[0]) == num_carte]
                    self.Show_Searched_Payements_A_Faire(liste_payements)
                    return
                else:
                    self.Info_Msg("Erreur","invalid input (Veuillez Entrer un numero de carte valide)")
                    return
            if (str(self.payements_a_faire_search_field.text()).isalpha()):
                ##check for name and prenom
                nom_or_prenom = str.lower(self.payements_a_faire_search_field.text())
                if (BACKEND.Validation.Isvalid_Name(nom_or_prenom)):
                    liste_payements = [elt for elt in PAYEMENTS_A_FAIRE if (str.lower(elt[1]) == nom_or_prenom or str.lower(elt[2]) == nom_or_prenom)]
                    self.Show_Searched_Payements_A_Faire(liste_payements)
                    return
                else:
                    self.Info_Msg("Erreur","invalid input (Veuillez Entrer un (nom ou prenom) valide)")
                    return
            else:
                self.Info_Msg("Erreur","invalid input (Veuillez Entrer (un nom ou un prenom ou numero de carte nationale) valide)")
                return

    def Search_Payement_Reussis(self):
        global PAYEMENTS_REUSSIS
        global PAYEMENTS_REUSSIS_FILTERED
        if (str(self.payements_reussis_search_field.text()).isspace() or str(self.payements_reussis_search_field.text()) == ""):
            PAYEMENTS_REUSSIS_FILTERED = PAYEMENTS_REUSSIS
            self.Show_Searched_Payements_Reussis(PAYEMENTS_REUSSIS)
            return
        else:
            if(str(self.payements_reussis_search_field.text()).isnumeric()):
                ##check for carte national
                num_carte = self.payements_reussis_search_field.text()
                if(BACKEND.Validation.Isvalid_NumCarteNationale(num_carte)):
                    liste_payements = [elt for elt in PAYEMENTS_REUSSIS if elt[0] == num_carte]
                    PAYEMENTS_REUSSIS_FILTERED = liste_payements
                    self.Show_Searched_Payements_Reussis(liste_payements)
                    return
                else:
                    self.Info_Msg("Erreur","invalid input (Veuillez Entrer un numero de carte valide)")
                    return
            if (str(self.payements_reussis_search_field.text()).isalpha()):
                ##check for name and prenom
                nom_or_prenom = str.lower(self.payements_reussis_search_field.text())
                if (BACKEND.Validation.Isvalid_Name(nom_or_prenom)):
                    liste_payements = [elt for elt in PAYEMENTS_REUSSIS if (str.lower(elt[1]) == nom_or_prenom or str.lower(elt[2]) == nom_or_prenom)]
                    PAYEMENTS_REUSSIS_FILTERED = liste_payements
                    self.Show_Searched_Payements_Reussis(liste_payements)
                    return
                else:
                    self.Info_Msg("Erreur","invalid input (Veuillez Entrer un (nom ou prenom) valide)")
                    return
            else:
                self.Info_Msg("Erreur","invalid input (Veuillez Entrer (un nom ou un prenom ou numero de carte nationale) valide)")
                return

        return liste_payements
    def Search_Credit(self):
        global CREDITS
        if (str(self.credit_recherche_field.text()).isspace() or str(self.credit_recherche_field.text()) == ""):
            self.Show_Searched_Credits(CREDITS)
            return
        else:
            if(str(self.credit_recherche_field.text()).isnumeric()):
                ##check for carte national
                num_carte = self.credit_recherche_field.text()
                if(BACKEND.Validation.Isvalid_NumCarteNationale(num_carte)):
                    liste_payements = [elt for elt in CREDITS if str(elt[0]) == num_carte]
                    self.Show_Searched_Credits(liste_payements)
                    return
                else:
                    self.Info_Msg("Erreur","invalid input (Veuillez Entrer un numero de carte valide)")
                    return
            if (str(self.credit_recherche_field.text()).isalpha()):
                ##check for name and prenom
                nom_or_prenom = str.lower(self.credit_recherche_field.text())
                if (BACKEND.Validation.Isvalid_Name(nom_or_prenom)):
                    liste_payements = [elt for elt in CREDITS if (str.lower(elt[1]) == nom_or_prenom or str.lower(elt[2]) == nom_or_prenom)]
                    self.Show_Searched_Credits(liste_payements)
                    return
                else:
                    self.Info_Msg("Erreur","invalid input (Veuillez Entrer un (nom ou prenom) valide)")
                    return
            else:
                self.Info_Msg("Erreur","invalid input (Veuillez Entrer (un nom ou un prenom ou numero de carte nationale) valide)")
                return

    def Payer_Payement_A_Faire(self):
        indexes = self.payements_a_faire_table.selectionModel().selectedRows()
        if(len(indexes) != 1):
            self.Info_Msg("Erreur","Veuillez selectionnez un seul employe pour le payer !")
            return
        index = indexes[0]
        payement_reussi = {}
        payement_reussi["ENTREPRISE_DU_TRAVAIL"] = USER_NAME
        payement_reussi["NUM_EMPLOYE"] = self.payements_a_faire_table.item(index.row(), 0).text()
        payement_reussi["DATE_PAYEMENT"] = str(TODAY)
        payement_reussi["PAYEMENT"] = self.payements_a_faire_table.item(index.row(), 9).text()
        BACKEND.PayementsManipulate.SetSuccessPayements(payement_reussi)
        BACKEND.PayementsManipulate.DeleteCurrentPayement(payement_reussi["ENTREPRISE_DU_TRAVAIL"],payement_reussi["NUM_EMPLOYE"])
        self.Sync_Date()
        return

    def Export_Payements_Reussi(self):
        global PAYEMENTS_REUSSIS_FILTERED

        payement_reussis = PAYEMENTS_REUSSIS_FILTERED
        NUM_EMP = [elt[0] for elt in payement_reussis]
        NOM = [elt[1] for elt in payement_reussis]
        PRENOM = [elt[2] for elt in payement_reussis]
        DATE_PAY = [elt[3] for elt in payement_reussis]
        PAYEMENT = [elt[4] for elt in payement_reussis]

        newDataFrame = pd.DataFrame()
        newDataFrame['NUM CARTE NATIONAL'] = NUM_EMP
        newDataFrame['NOM'] = NOM
        newDataFrame['PRENOM'] = PRENOM
        newDataFrame['DATE PAYEMENT'] = DATE_PAY
        newDataFrame['PAYEMENT'] = PAYEMENT
        file_name = QFileDialog.getSaveFileName(self,"save file",None,".xlsx")
        if(file_name[0] == ""):
            return
        newDataFrame.to_excel(f'{file_name[0]}_{datetime.now().date()}_{str(datetime.now().time()).replace(":","").split(".")[0]}.xlsx', index = False)
        return
        

        

if __name__ == '__main__':

    ##PREPARE DATA FROM DB
    Load_User()
    app = QApplication(sys.argv)
    window = Main()
    window.showMaximized()
    app.exec_()

