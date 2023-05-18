import sqlite3
from datetime import date,datetime,timedelta
import pickle

DATA_BASE = "./BACKEND/data"
TODAY = datetime.today().strftime('%d/%m/%Y')

def Load_User():
    global USER_NAME
    fp = open("entreprise.pkl","rb")
    data = pickle.load(fp)
    USER_NAME = data["username"]
    fp.close()

def Info_Msg(title,content,type):
   info_msg={}
   info_msg["title"] = title 
   info_msg["content"] = content
   info_msg["type"] = type
   return info_msg


USER_NAME = ""
TODAY = datetime.today().strftime('%d/%m/%Y')


def DateDifference(date1 , date2):
    d1 = datetime.strptime(date1, "%d/%m/%Y")
    d2 = datetime.strptime(date2, "%d/%m/%Y")
    diffrence = d1 - d2
    return diffrence.days


def Total_To_Pay(salary,total_work_days,avance,absence):
    salary = float(salary.replace(",",""))
    day_salary = salary / 30.
    to_pay = (day_salary * float(total_work_days) - float(avance))
    ##(f"{to_pay:,}")
    return f"{to_pay:,}"


def SetDefaultPayement(employee):
    Load_User()
    date_of_employement = datetime.strptime(employee["date_debut_travail"], "%d/%m/%Y")
    today = datetime.strptime(TODAY, "%d/%m/%Y")
    next_payement_day = datetime.strftime(date_of_employement + timedelta(30),"%d/%m/%Y")
    Previous_Date = datetime.today() - timedelta(days=1)
    PAYEMENT_EN_COURS={}
    PAYEMENT_EN_COURS["ENTREPRISE_DU_TRAVAIL"] = USER_NAME
    PAYEMENT_EN_COURS["NUM_EMPLOYE"] = employee["num_carte_nationale"]
    PAYEMENT_EN_COURS["DATE_PROCHAIN_PAYEMENT"] = next_payement_day
    PAYEMENT_EN_COURS["PRESENCE_AUJOURDHUI"] = "NON"
    PAYEMENT_EN_COURS["LAST_PRESENCE_CHECK"] = Previous_Date.strftime('%d/%m/%Y')
    PAYEMENT_EN_COURS["ABSENCE"] = 0
    PAYEMENT_EN_COURS["AVANCE"] = 0
    PAYEMENT_EN_COURS["TOTAL_JOURS_TRAVAIL"] = 0
    PAYEMENT_EN_COURS["SALAIRE"] = employee["salaire"]
    PAYEMENT_EN_COURS["TOTAL_A_PAYER"] = Total_To_Pay(employee["salaire"],0,0,0)
    SetCurrentPayements(PAYEMENT_EN_COURS)


def SetCurrentPayements(payment):
    Response = {}
    connection = sqlite3.connect(f"{DATA_BASE}/gestion_employes.db")
    cursor = connection.cursor()
    if not connection:
        Response = Info_Msg("Erreur Conncetion","Erreur Inatendu a la connection !","error")
        return Response
    ##query = 
    try:       
        sqlite_insert_query = f"""INSERT INTO PAYEMENT_EN_COURS
                            (
                                ENTREPRISE_DU_TRAVAIL,
                                NUM_EMPLOYE,
                                DATE_PROCHAIN_PAYEMENT,
                                PRESENCE_AUJOURDHUI,
                                LAST_PRESENCE_CHECK,
                                ABSENCE,
                                TOTAL_JOURS_TRAVAIL,
                                SALAIRE,
                                AVANCE,
                                TOTAL_A_PAYER
                            ) 
                            VALUES 
                            (
                                "{payment["ENTREPRISE_DU_TRAVAIL"]}",
                                "{payment["NUM_EMPLOYE"]}",
                                "{payment["DATE_PROCHAIN_PAYEMENT"]}",
                                "{payment["PRESENCE_AUJOURDHUI"]}",
                                "{payment["LAST_PRESENCE_CHECK"]}",
                                "{payment["ABSENCE"]}",
                                "{payment["TOTAL_JOURS_TRAVAIL"]}",
                                "{payment["SALAIRE"]}",
                                "{payment["AVANCE"]}",
                                "{payment["TOTAL_A_PAYER"]}"
                            )"""

        count = cursor.execute(sqlite_insert_query)
        connection.commit()
        cursor.close()
        Response = Info_Msg("Ajout avec Succes","Payement En Cours Ajoute avec Succes","success")
        return Response
        
    except sqlite3.Error as error:
       ## print("Failed to insert data into sqlite table", error)
        Response = Info_Msg("Ajout Echoue","veuillez reesseyer l'ajout du payement en cours","error")
        return Response


def CheckCurrentPayements(username):
    def Check_Payement(last_presence_date):
        d1 = datetime.strptime(TODAY, '%d/%m/%Y')
        d2 = datetime.strptime(last_presence_date, '%d/%m/%Y')
        delta = d1 - d2
        if (delta.days >= 2):
            return False
        else:
            return True

    def setRetard(date2):
        return DateDifference(TODAY,date2)


    def setNextPayement(date):
        next_date = datetime.strptime(date, "%d/%m/%Y")      
        return (str(datetime.strftime(next_date+timedelta(30),"%d/%m/%Y")))

    def setDays(salary,credit):
        emp_salary = "{:.3f}".format(float(str(salary).replace(",","")))
        credit_to_pay = "{:.3f}".format(abs(float(str(credit).replace(",",""))))
        day_salary = float(emp_salary) / 30.    
        to_pay = "{:.1f}".format(float(credit_to_pay) / float(day_salary))
        return (round(float(to_pay)))

    def setCredit(payement):
        credit = abs(float(str(payement).replace(",","")))
        return f"{credit:,}"

    def isCredit(x):
        credit = float(str(x).replace(",",""))
        return (credit < 0)
    
    def isPayement(x):
        payment = float(str(x).replace(",",""))
        return (payment>=0)

    connection = sqlite3.connect(f"{DATA_BASE}/gestion_employes.db")
    connection.create_function("check_payement",1,Check_Payement)
    connection.create_function("retard",1,setRetard)
    connection.create_function("next_pay",1,setNextPayement)
    connection.create_function("set_days",2,setDays)
    connection.create_function("set_credit",1,setCredit)
    connection.create_function("isCredit",1,isCredit)
    connection.create_function("isPayement",1,isPayement)
    cursor = connection.cursor()
    try:
        ##print("here")
        main_query = f'''
                SELECT 
                    NUM_EMPLOYE,
                    ENTREPRISE_DU_TRAVAIL,
                    LAST_PRESENCE_CHECK
                FROM 
                    PAYEMENT_EN_COURS
                WHERE
                    check_payement(LAST_PRESENCE_CHECK) = {False} 
                    AND
                    ENTREPRISE_DU_TRAVAIL = '{username}';   
            '''
        results = cursor.execute(main_query).fetchall()
        connection.commit()
        ##print(results)
        if (len(results) > 0):
            for employe in results:
                query = []
                query.append(
                    f'''
                        UPDATE "EMPLOYE"
                        SET 
                            DATE_ARRET_TRAVAIL = "{employe[2]}"
                        WHERE
                            ENTREPRISE_DU_TRAVAIL = '{username}'
                            AND
                            NUM_CARTE_NATIONALE = '{employe[0]}';                    
                    '''
                )
                query.append(
                    f'''
                        UPDATE "PAYEMENT_EN_COURS"
                        SET 
                            DATE_PROCHAIN_PAYEMENT = "{employe[2]}"
                        WHERE
                            ENTREPRISE_DU_TRAVAIL = '{username}'
                            AND
                            NUM_EMPLOYE = '{employe[0]}';
                    '''
                )
            
                query.append(
                    f'''INSERT INTO "CREDITS"
                        (
                            ENTREPRISE_DU_TRAVAIL,
                            NUM_EMPLOYE,
                            CREDIT,
                            EN_JOURS_DE_TRAVAIL,
                            DATE_CREDITS
                        )
                        SELECT        
                            ENTREPRISE_DU_TRAVAIL,
                            NUM_EMPLOYE,
                            set_credit(TOTAL_A_PAYER),
                            set_days(SALAIRE,TOTAL_A_PAYER),
                            "{TODAY}"
                        FROM "PAYEMENT_EN_COURS"
                        WHERE
                            ENTREPRISE_DU_TRAVAIL = "{username}"
                            AND
                            NUM_EMPLOYE = '{employe[0]}'
                            AND
                            isCredit(TOTAL_A_PAYER) = {True};
                    '''
                )
                query.append(
                    f'''INSERT INTO "PAYEMENT_A_PAYER"
                        (
                            ENTREPRISE_DU_TRAVAIL,
                            NUM_EMPLOYE,
                            DATE_DU_PAYEMENT,
                            RETARD_DU_PAYEMENT,
                            SALAIRE,
                            ABSENCE,
                            TOTAL_JOURS_TRAVAIL,
                            AVANCE,
                            PAYEMENT
                        )
                        SELECT        
                            ENTREPRISE_DU_TRAVAIL,
                            NUM_EMPLOYE,
                            DATE_PROCHAIN_PAYEMENT,
                            "0",
                            SALAIRE,
                            ABSENCE,
                            TOTAL_JOURS_TRAVAIL,
                            AVANCE,
                            TOTAL_A_PAYER
                        FROM "PAYEMENT_EN_COURS"
                        WHERE
                            ENTREPRISE_DU_TRAVAIL = "{username}"
                            AND
                            NUM_EMPLOYE = '{employe[0]}'
                            AND
                            isPayement(TOTAL_A_PAYER) = {True};
                    '''
                )
                query.append(
                    f'''DELETE FROM "PAYEMENT_EN_COURS"
                        WHERE
                            ENTREPRISE_DU_TRAVAIL = "{username}"
                            AND
                            NUM_EMPLOYE = '{employe[0]}'
                    '''
                )
                query.append(
                    f'''DELETE FROM "LISTE_PRESENCE"
                        WHERE
                            ENTREPRISE_DU_TRAVAIL = "{username}"
                            AND
                            NUM_EMPLOYE = '{employe[0]}'
                    '''
                )

                for i in range(len(query)):
                    cursor.execute(query[i])
                    connection.commit()                
        cursor.close()
        Response = Info_Msg("Succes","Presence faite avec Succes","success")
        return Response

    except sqlite3.Error as error:
        ##print("Failed to update data into sqlite table", error)
        Response = Info_Msg("Erreur","Echec de Faire cette Presence","error")
        return Response    


def UpdateAvanceInCurrentPayement(nouvelle_avance):
    connection = sqlite3.connect(f"{DATA_BASE}/gestion_employes.db")
    cursor = connection.cursor()
    query = f'''UPDATE "PAYEMENT_EN_COURS"
                    SET
                    AVANCE = {nouvelle_avance["AVANCE"]},
                    TOTAL_A_PAYER = {float(Total_To_Pay(nouvelle_avance["SALAIRE"],nouvelle_avance["TOTAL_JOURS_TRAVAIL"],nouvelle_avance["AVANCE"],0).replace(",",""))}
                WHERE 
                    ENTREPRISE_DU_TRAVAIL="{nouvelle_avance["ENTREPRISE_DU_TRAVAIL"]}"
                        AND
                    NUM_EMPLOYE == "{nouvelle_avance["NUM_EMPLOYE"]}";
                '''
    results = cursor.execute(query)
    connection.commit()
    Response = Info_Msg("Succes","Avance Attribue(s) avec Succes Au L'employe","success")
    return Response


def UpdatePresenceInCurrentPayement(presences):
    connection = sqlite3.connect(f"{DATA_BASE}/gestion_employes.db")
    connection.create_function("update_payement",4,Total_To_Pay)
    cursor = connection.cursor()
    for presence in presences:
        presence = list(presence)
        query = f'''
                    SELECT 
                        LAST_PRESENCE_CHECK 
                    FROM 
                        PAYEMENT_EN_COURS
                    WHERE
                        ENTREPRISE_DU_TRAVAIL = "{presence[0]}"
                        AND
                        NUM_EMPLOYE = "{presence[1]}";    
                '''
        result = cursor.execute(query).fetchall()
        connection.commit()
        result = list(result[0])[0]
        absence = 0 if (presence[4] == "OUI") else 1
        last_presence = str(presence[2]) if (presence[3] == "OUI") else str(result)
        query = f'''UPDATE PAYEMENT_EN_COURS
                    SET 
                        TOTAL_JOURS_TRAVAIL = TOTAL_JOURS_TRAVAIL + {presence[5]},
                        ABSENCE = ABSENCE + {absence},
                        TOTAL_A_PAYER = update_payement(SALAIRE,TOTAL_JOURS_TRAVAIL,AVANCE,ABSENCE),
                        PRESENCE_VALIDE = "NON",
                        PRESENCE_AUJOURDHUI = "NON",
                        LAST_PRESENCE_CHECK = "{last_presence}"
                    WHERE
                        ENTREPRISE_DU_TRAVAIL = "{presence[0]}"
                        AND
                        NUM_EMPLOYE = "{presence[1]}";
                '''
        results = cursor.execute(query)
        connection.commit()
    cursor.close()
    return


def UpdateNextPayementDateInCurrentPayement(username):
    def setRetard(date2):
        return DateDifference(TODAY,date2)


    def setNextPayement(date):
        next_date = datetime.strptime(date, "%d/%m/%Y")      
        return (str(datetime.strftime(next_date+timedelta(30),"%d/%m/%Y")))

    def setDays(salary,credit):
        emp_salary = "{:.3f}".format(float(str(salary).replace(",","")))
        credit_to_pay = "{:.3f}".format(abs(float(str(credit).replace(",",""))))
        day_salary = float(emp_salary) / 30.    
        to_pay = "{:.1f}".format(float(credit_to_pay) / float(day_salary))
        return (round(float(to_pay)))

    def setCredit(payement):
        credit = abs(float(str(payement).replace(",","")))
        return f"{credit:,}"

    def isCredit(x):
        credit = float(str(x).replace(",",""))
        return (credit < 0)
    
    def isPayement(x):
        payment = float(str(x).replace(",",""))
        return (payment>=0)

    connection = sqlite3.connect(f"{DATA_BASE}/gestion_employes.db")
    connection.create_function("retard",1,setRetard)
    connection.create_function("next_pay",1,setNextPayement)
    connection.create_function("set_days",2,setDays)
    connection.create_function("set_credit",1,setCredit)
    connection.create_function("isCredit",1,isCredit)
    connection.create_function("isPayement",1,isPayement)
    cursor = connection.cursor()

    query = []

    query.append(
        f'''INSERT INTO "CREDITS"
            (
                ENTREPRISE_DU_TRAVAIL,
                NUM_EMPLOYE,
                CREDIT,
                EN_JOURS_DE_TRAVAIL,
                DATE_CREDITS
            )
            SELECT        
                ENTREPRISE_DU_TRAVAIL,
                NUM_EMPLOYE,
                set_credit(TOTAL_A_PAYER),
                set_days(SALAIRE,TOTAL_A_PAYER),
                "{TODAY}"
            FROM "PAYEMENT_EN_COURS"
            WHERE
                ENTREPRISE_DU_TRAVAIL = "{username}"
                AND
                retard(DATE_PROCHAIN_PAYEMENT) = 0
                AND
                isCredit(TOTAL_A_PAYER) = {True};
        '''
    )
    query.append(
        f'''INSERT INTO "PAYEMENT_A_PAYER"
            (
                ENTREPRISE_DU_TRAVAIL,
                NUM_EMPLOYE,
                DATE_DU_PAYEMENT,
                RETARD_DU_PAYEMENT,
                SALAIRE,
                ABSENCE,
                TOTAL_JOURS_TRAVAIL,
                AVANCE,
                PAYEMENT
            )
            SELECT        
                ENTREPRISE_DU_TRAVAIL,
                NUM_EMPLOYE,
                DATE_PROCHAIN_PAYEMENT,
                "0",
                SALAIRE,
                ABSENCE,
                TOTAL_JOURS_TRAVAIL,
                AVANCE,
                TOTAL_A_PAYER
            FROM "PAYEMENT_EN_COURS"
            WHERE
                ENTREPRISE_DU_TRAVAIL = "{username}"
                AND
                retard(DATE_PROCHAIN_PAYEMENT) = 0
                AND
                isPayement(TOTAL_A_PAYER) = {True};
        '''
    )

    query.append(
        f'''UPDATE "PAYEMENT_EN_COURS"
                SET 
                    TOTAL_JOURS_TRAVAIL = 0.0,
                    ABSENCE = 0,
                    AVANCE = 0.0
                WHERE
                    ENTREPRISE_DU_TRAVAIL = "{username}"
                    AND
                    retard(DATE_PROCHAIN_PAYEMENT) = 0;
                '''
    )

    query.append(
            f'''
                UPDATE "PAYEMENT_EN_COURS"
                SET 
                    DATE_PROCHAIN_PAYEMENT = next_pay(DATE_PROCHAIN_PAYEMENT),
                    TOTAL_A_PAYER = 0.0
                WHERE
                    ENTREPRISE_DU_TRAVAIL = "{username}"
                    AND
                    retard(DATE_PROCHAIN_PAYEMENT) = 0
                    AND
                    TOTAL_JOURS_TRAVAIL = 0.0
                    AND
                    ABSENCE = 0
                    AND
                    AVANCE = 0.0;
                '''
    )

    for i in range(len(query)):

        cursor.execute(query[i])
        connection.commit()
    cursor.close()
    return



def UpdateRetardPayemenetInPendingPayement(username):
    def setRetard(date2):
        return DateDifference(TODAY,date2)

    connection = sqlite3.connect(f"{DATA_BASE}/gestion_employes.db")
    connection.create_function("retard",1,setRetard)
    cursor = connection.cursor()
    query = f'''UPDATE PAYEMENT_A_PAYER
                SET
                    RETARD_DU_PAYEMENT = retard(DATE_DU_PAYEMENT)
                WHERE 
                    ENTREPRISE_DU_TRAVAIL="{username}"
                '''
    connection.execute(query)
    connection.commit()
    return


def DeleteCurrentPayement(username,num_employe):
    connection = sqlite3.connect(f"{DATA_BASE}/gestion_employes.db")
    cursor = connection.cursor()
    query = f'''DELETE 
                FROM 
                    "PAYEMENT_A_PAYER" 
                WHERE 
                    ENTREPRISE_DU_TRAVAIL="{username}"
                    AND
                    NUM_EMPLOYE = {num_employe}
                '''
    connection.execute(query)
    connection.commit()
    return

def DeleteCredit(username,credit):
    connection = sqlite3.connect(f"{DATA_BASE}/gestion_employes.db")
    cursor = connection.cursor()
    query = f'''DELETE 
                FROM 
                    "CREDITS" 
                WHERE 
                    ENTREPRISE_DU_TRAVAIL="{username}"
                    AND
                    NUM_EMPLOYE = {credit["num_employe"]}
                    AND
                    DATE_CREDITS = "{credit["date_credits"]}"
                '''
    connection.execute(query)
    connection.commit()
    return

def SetSuccessPayements(payment):
    Response = {}
    ##try to connect to db
    connection = sqlite3.connect(f"{DATA_BASE}/gestion_employes.db")
    cursor = connection.cursor()
    if not connection:
        Response = Info_Msg("Erreur Conncetion","Erreur Inatendu a la connection !","error")
        return Response
    ##query = 
    try:       
        sqlite_insert_query = f"""INSERT INTO PAYEMENT_REUSSI
                            (
                                ENTREPRISE_DU_TRAVAIL,
                                NUM_EMPLOYE,
                                DATE_PAYEMENT,
                                PAYEMENT
                            ) 
                            VALUES 
                            (
                                "{payment["ENTREPRISE_DU_TRAVAIL"]}",
                                "{payment["NUM_EMPLOYE"]}",
                                "{payment["DATE_PAYEMENT"]}",
                                "{payment["PAYEMENT"]}"
                            )"""

        count = cursor.execute(sqlite_insert_query)
        connection.commit()
        cursor.close()
        Response = Info_Msg("Ajout avec Succes","Payemenyt Reussie Ajoute avec Succes","success")
        return Response
        
    except sqlite3.Error as error:
        ##print("Failed to insert data into sqlite table", error)
        Response = Info_Msg("Ajout Echoue","veuillez reesseyer l'ajout du payement reussi","error")
        return Response


def Show_Payements_En_Cours(username):
    connection = sqlite3.connect(f"{DATA_BASE}/gestion_employes.db")
    cursor = connection.cursor()
    query = f'''SELECT 
                    "PAYEMENT_EN_COURS".NUM_EMPLOYE,
                    "EMPLOYE".NOM,
                    "EMPLOYE".PRENOM,
                    "PAYEMENT_EN_COURS".DATE_PROCHAIN_PAYEMENT,
                    "PAYEMENT_EN_COURS".ABSENCE,
                    "PAYEMENT_EN_COURS".TOTAL_JOURS_TRAVAIL,
                    "PAYEMENT_EN_COURS".SALAIRE,
                    "PAYEMENT_EN_COURS".AVANCE,
                    "PAYEMENT_EN_COURS".TOTAL_A_PAYER,
                    "PAYEMENT_EN_COURS".PRESENCE_VALIDE
                FROM 
                    "EMPLOYE" 
                        INNER JOIN 
                    "PAYEMENT_EN_COURS"
                        ON
                        "EMPLOYE".NUM_CARTE_NATIONALE = "PAYEMENT_EN_COURS".NUM_EMPLOYE
                            AND
                        "EMPLOYE".ENTREPRISE_DU_TRAVAIL = "PAYEMENT_EN_COURS".ENTREPRISE_DU_TRAVAIL
                WHERE 
                    "EMPLOYE".ENTREPRISE_DU_TRAVAIL="{username}"
                        AND
                    "EMPLOYE".DATE_ARRET_TRAVAIL == "EN_TRAVAIL"    
                '''
    results = connection.execute(query).fetchall()
    connection.commit()
    return results

def Show_Payements_A_Faire(username):
    connection = sqlite3.connect(f"{DATA_BASE}/gestion_employes.db")
    cursor = connection.cursor()
    query = f'''SELECT 
                    "PAYEMENT_A_PAYER".NUM_EMPLOYE,
                    "EMPLOYE".NOM,
                    "EMPLOYE".PRENOM,
                    "PAYEMENT_A_PAYER".DATE_DU_PAYEMENT,
                    "PAYEMENT_A_PAYER".RETARD_DU_PAYEMENT,
                    "PAYEMENT_A_PAYER".SALAIRE,
                    "PAYEMENT_A_PAYER".ABSENCE,
                    "PAYEMENT_A_PAYER".TOTAL_JOURS_TRAVAIL,
                    "PAYEMENT_A_PAYER".AVANCE,
                    "PAYEMENT_A_PAYER".PAYEMENT
                FROM 
                    "PAYEMENT_A_PAYER" 
                        INNER JOIN 
                    "EMPLOYE"
                        ON
                        "EMPLOYE".NUM_CARTE_NATIONALE = "PAYEMENT_A_PAYER".NUM_EMPLOYE
                            AND
                        "EMPLOYE".ENTREPRISE_DU_TRAVAIL = "PAYEMENT_A_PAYER".ENTREPRISE_DU_TRAVAIL
                WHERE 
                    "EMPLOYE".ENTREPRISE_DU_TRAVAIL="{username}";
    
                '''
##  AND "EMPLOYE".DATE_ARRET_TRAVAIL == "EN_TRAVAIL";
    results = connection.execute(query).fetchall()
    connection.commit()
    return results

def Show_Credits(username):
    connection = sqlite3.connect(f"{DATA_BASE}/gestion_employes.db")
    cursor = connection.cursor()
##  AND "EMPLOYE".DATE_ARRET_TRAVAIL == "EN_TRAVAIL";
    query = f'''SELECT 
                    "CREDITS".NUM_EMPLOYE,
                    "EMPLOYE".NOM,
                    "EMPLOYE".PRENOM,
                    "CREDITS".CREDIT,
                    "CREDITS".EN_JOURS_DE_TRAVAIL,
                    "CREDITS".DATE_CREDITS
                FROM 
                    "CREDITS" 
                        INNER JOIN 
                    "EMPLOYE"
                        ON
                        "EMPLOYE".NUM_CARTE_NATIONALE = "CREDITS".NUM_EMPLOYE
                            AND
                        "EMPLOYE".ENTREPRISE_DU_TRAVAIL = "CREDITS".ENTREPRISE_DU_TRAVAIL
                WHERE 
                    "EMPLOYE".ENTREPRISE_DU_TRAVAIL="{username}";   
                '''
    results = connection.execute(query).fetchall()
    connection.commit()
    return results

def Show_Payements_Reussis(username):
    connection = sqlite3.connect(f"{DATA_BASE}/gestion_employes.db")
    cursor = connection.cursor()
##  AND "EMPLOYE".DATE_ARRET_TRAVAIL == "EN_TRAVAIL";
    query = f'''SELECT 
                    "PAYEMENT_REUSSI".NUM_EMPLOYE,
                    "EMPLOYE".NOM,
                    "EMPLOYE".PRENOM,
                    "PAYEMENT_REUSSI".DATE_PAYEMENT,
                    "PAYEMENT_REUSSI".PAYEMENT
                FROM 
                    "PAYEMENT_REUSSI" 
                        INNER JOIN 
                    "EMPLOYE"
                        ON
                        "EMPLOYE".NUM_CARTE_NATIONALE = "PAYEMENT_REUSSI".NUM_EMPLOYE
                            AND
                        "EMPLOYE".ENTREPRISE_DU_TRAVAIL = "PAYEMENT_REUSSI".ENTREPRISE_DU_TRAVAIL
                WHERE 
                    "EMPLOYE".ENTREPRISE_DU_TRAVAIL="{username}";   
                '''
    results = connection.execute(query).fetchall()
    connection.commit()
    return results