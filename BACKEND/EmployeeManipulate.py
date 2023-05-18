import sqlite3
from datetime import date,datetime,timedelta

DATA_BASE = "./BACKEND/data"
TODAY = datetime.today().strftime('%d/%m/%Y')

def Info_Msg(title,content,type):
   info_msg={}
   info_msg["title"] = title 
   info_msg["content"] = content
   info_msg["type"] = type
   return info_msg


def DateDifference(date1 , date2):
    d1 = datetime.strptime(date1, "%d/%m/%Y")
    d2 = datetime.strptime(date2, "%d/%m/%Y")
    diffrence = d1 - d2
    return diffrence.days

def Add_Employee(employee):
    Response = {}
    ##try to connect to db
    connection = sqlite3.connect(f"{DATA_BASE}/gestion_employes.db")
    cursor = connection.cursor()
    if not connection:
        Response = Info_Msg("Erreur Conncetion","Erreur Inatendu a la connection !","error")
        return Response
    ##query = 
    try:       
        sqlite_insert_query = f"""INSERT INTO EMPLOYE
                            (
                                NOM,
                                PRENOM,
                                NUM_TEL,
                                ENTREPRISE_DU_TRAVAIL,
                                DATE_NAISSANCE,
                                ADDRESSE,
                                NUM_CARTE_NATIONALE,
                                DATE_EMPLOYEMENT,
                                DATE_DEBUT_TRAVAIL,
                                DATE_ARRET_TRAVAIL,
                                SALAIRE,
                                OBSERVATION
                            ) 
                            VALUES 
                            (
                                "{employee["nom"]}",
                                "{employee["prenom"]}",
                                "{employee["num_tel"]}",
                                "{employee["entreprise_de_travail"]}",
                                "{employee["date_naissance"]}",
                                "{employee["addresse"]}",
                                "{employee["num_carte_nationale"]}",
                                "{employee["date_debut_travail"]}",
                                "{employee["date_debut_travail"]}",
                                "{employee["date_fin_travail"]}",
                                "{employee["salaire"]}",
                                "{employee["observation"]}"
                            )"""

        count = cursor.execute(sqlite_insert_query)
        connection.commit()
        cursor.close()
        Response = Info_Msg("Ajout avec Succes","Employee Ajoute avec Succes","success")
        return Response
        
    except sqlite3.Error as error:
        ##print("Failed to insert data into sqlite table", error)
        Response = Info_Msg("Erreur","Employe avec la meme Numero Carte Nationale est deja inscirt !!!","error")
        return Response

def Delete_Employe(username,list_employees_ids):
    connection = sqlite3.connect(f"{DATA_BASE}/gestion_employes.db")
    connection.execute("PRAGMA FOREIGN_KEYS = ON")
    cursor = connection.cursor()
    ##print(f"delete {username} {list_employees_ids}")
    try:
        sqlite_delete_query = f'''
                DELETE FROM EMPLOYE
                WHERE 
                NUM_CARTE_NATIONALE
                IN
                ({list_employees_ids})    
                AND 
                ENTREPRISE_DU_TRAVAIL = '{username}'
            '''
        queries = []
        queries.append(
            f'''
                DELETE FROM LISTE_PRESENCE
                WHERE 
                NUM_EMPLOYE
                IN
                ({list_employees_ids})    
                AND 
                ENTREPRISE_DU_TRAVAIL = '{username}';
            '''
        )
        queries.append(
            f'''
                DELETE FROM PAYEMENT_A_PAYER
                WHERE 
                NUM_EMPLOYE
                IN
                ({list_employees_ids})    
                AND 
                ENTREPRISE_DU_TRAVAIL = '{username}';
            '''
        )
        queries.append(
            f'''
                DELETE FROM PAYEMENT_EN_COURS
                WHERE 
                NUM_EMPLOYE
                IN
                ({list_employees_ids})    
                AND 
                ENTREPRISE_DU_TRAVAIL = '{username}';
            '''
        )
        queries.append(
            f'''
                DELETE FROM PAYEMENT_REUSSI
                WHERE 
                NUM_EMPLOYE
                IN
                ({list_employees_ids})    
                AND 
                ENTREPRISE_DU_TRAVAIL = '{username}';
            '''
        )
        queries.append(
            f'''
                DELETE FROM CREDITS
                WHERE 
                NUM_EMPLOYE
                IN
                ({list_employees_ids})    
                AND 
                ENTREPRISE_DU_TRAVAIL = '{username}';
            '''
        )
        count = cursor.execute(sqlite_delete_query)
        connection.commit()
        for i in range(len(queries)):
            cursor.execute(queries[i])
            connection.commit()
        cursor.close()
        Response = Info_Msg("Suppresion avec Succes","Employe(s) Supprime(s) avec Succes","success")
        return Response
        
    except sqlite3.Error as error:
        ##print("Failed to delete data into sqlite table", error)
        Response = Info_Msg("Suppression Echoue","veuillez reesseyer la Suppression de(s) l'employe(s)","error")
        return Response
    

def Update_Employee(username,new_employee,employe_id):

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
    try:
        sqlite_delete_query = f'''
                SELECT
                    NUM_CARTE_NATIONALE,  
                    DATE_ARRET_TRAVAIL,
                    DATE_DEBUT_TRAVAIL
                FROM 
                    EMPLOYE
                WHERE
                    NUM_CARTE_NATIONALE = '{employe_id}'
                    AND
                    ENTREPRISE_DU_TRAVAIL = '{username}';   
            '''
        results = cursor.execute(sqlite_delete_query).fetchall()
        connection.commit()

        results = list(results[0])
        if (len(results)>0):

            query = f'''
            UPDATE EMPLOYE
            SET 
                ADDRESSE = "{new_employee['addresse']}",
                SALAIRE = "{new_employee['salaire']}",
                OBSERVATION = "{new_employee['observation']}",
                NUM_TEL = "{new_employee["num_tel"]}"
            WHERE
                NUM_CARTE_NATIONALE = '{employe_id}'
                AND
                ENTREPRISE_DU_TRAVAIL = '{username}';'''
            cursor.execute(query)
            connection.commit()
            query = f'''
            UPDATE PAYEMENT_EN_COURS
            SET 
                SALAIRE = "{new_employee['salaire']}"
            WHERE
                NUM_EMPLOYE = '{employe_id}'
                AND
                ENTREPRISE_DU_TRAVAIL = '{username}';'''
            cursor.execute(query)
            connection.commit()

            ##was in work then it stopped today
            if(results[1] == "EN_TRAVAIL" and new_employee["date_fin_travail"] != "EN_TRAVAIL"):
                query = []
                if(DateDifference(results[2],new_employee["date_fin_travail"]) == 0):
                   ##print("here")
                   Response = Info_Msg("Erreur","Employe(s) a deja commencer le travail aujourdhui","error")
                   return Response         
                query.append(
                    f'''    
                        UPDATE EMPLOYE
                        SET 
                            DATE_ARRET_TRAVAIL = "{TODAY}"
                        WHERE
                            NUM_CARTE_NATIONALE = '{employe_id}'
                            AND
                            ENTREPRISE_DU_TRAVAIL = '{username}';                    
                    
                    '''
                )
                query.append(
                    f'''
                        UPDATE PAYEMENT_EN_COURS
                        SET 
                            DATE_PROCHAIN_PAYEMENT = "{TODAY}"
                        WHERE
                            ENTREPRISE_DU_TRAVAIL = '{username}'
                            AND
                            NUM_EMPLOYE = "{employe_id}";
                    '''
                )
                query.append(
                    f'''INSERT INTO CREDITS
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
                            NUM_EMPLOYE = "{employe_id}"
                            AND
                            isCredit(TOTAL_A_PAYER) = {True};
                    '''
                )
                query.append(
                    f'''INSERT INTO PAYEMENT_A_PAYER
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
                            "{TODAY}",
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
                            NUM_EMPLOYE = "{employe_id}"
                            AND
                            isPayement(TOTAL_A_PAYER) = {True};
                    '''
                )
                query.append(
                    f'''DELETE FROM PAYEMENT_EN_COURS
                        WHERE
                            ENTREPRISE_DU_TRAVAIL = "{username}"
                            AND
                            NUM_EMPLOYE = "{employe_id}"
                    '''
                )
                query.append(
                    f'''DELETE FROM LISTE_PRESENCE
                        WHERE
                            ENTREPRISE_DU_TRAVAIL = "{username}"
                            AND
                            NUM_EMPLOYE = "{employe_id}"
                    '''
                )
                for i in range (len(query)):
                    count = cursor.execute(query[i])
                    connection.commit()

            ##was off work then it comes back to work today
            elif(results[1] != "EN_TRAVAIL" and new_employee["date_fin_travail"] == "EN_TRAVAIL"):
                if(DateDifference(TODAY,results[1]) == 0):
                    Response = Info_Msg("Erreur","Employe(s) a deja arreter le travail aujourdhui","error")
                    return Response   
                ##print("****here*****")                 
                query = []
                salaire = ""
                date_fin_travail = ""
                date_next_payement = setNextPayement(TODAY)
                query2 = f'''
                    SELECT 
                        SALAIRE,
                        DATE_ARRET_TRAVAIL
                    FROM 
                        EMPLOYE
                    WHERE
                        NUM_CARTE_NATIONALE = "{employe_id}"
                        AND
                        ENTREPRISE_DU_TRAVAIL = "{username}"
                    '''
                result = cursor.execute(query2).fetchall()
                connection.commit()
                result = list(result[0])
                ##date_fin_travail = str(result[1])
                salaire = str(result[0])
                last_presence_check =  (datetime.today() - timedelta(days=1)).strftime('%d/%m/%Y')
                query.append(
                    f'''
                        UPDATE "EMPLOYE"
                        SET 
                            ADDRESSE = "{new_employee['addresse']}",
                            SALAIRE = "{new_employee['salaire']}",
                            DATE_ARRET_TRAVAIL = "EN_TRAVAIL",
                            DATE_DEBUT_TRAVAIL = "{TODAY}",
                            OBSERVATION = "{new_employee['observation']}"
                        WHERE
                            NUM_CARTE_NATIONALE = "{employe_id}"
                            AND
                            ENTREPRISE_DU_TRAVAIL = "{username}"
                            ;
                    '''                            
                )
                query.append(
                        f'''INSERT INTO PAYEMENT_EN_COURS
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
                                "{username}",
                                "{employe_id}",
                                "{date_next_payement}",
                                "NON",
                                "{last_presence_check}",
                                0,
                                0,
                                "{salaire}",
                                0,
                                0
                            )'''
                )
                for i in range (len(query)):
                    ##print(f"********* {i} ***********")
                    count = cursor.execute(query[i])
                    connection.commit()
        cursor.close()
        Response = Info_Msg("Modification avec Succes","Employe(s) Modifie(s) avec Succes","success")
        return Response
        
    except sqlite3.Error as error:
        ##print("Failed to delete data into sqlite table", error)
        Response = Info_Msg("Modification Echoue","veuillez reesseyer la Modification de l'employe","error")
        return Response    

def Show_Employees(username):
    connection = sqlite3.connect(f"{DATA_BASE}/gestion_employes.db")
    cursor = connection.cursor()
    query = f'''SELECT "NOM","PRENOM","NUM_TEL","DATE_NAISSANCE","ADDRESSE","NUM_CARTE_NATIONALE","DATE_EMPLOYEMENT","DATE_ARRET_TRAVAIL","SALAIRE","OBSERVATION" 
                FROM "EMPLOYE" 
                WHERE "ENTREPRISE_DU_TRAVAIL"="{username}"'''
    results = connection.execute(query).fetchall()
    connection.commit()
    return results

    