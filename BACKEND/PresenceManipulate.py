import sqlite3
from datetime import datetime,timedelta

DATA_BASE = "./BACKEND/data"

TODAY = datetime.today().strftime('%d/%m/%Y')

def Info_Msg(title,content,type):
   info_msg={}
   info_msg["title"] = title 
   info_msg["content"] = content
   info_msg["type"] = type
   return info_msg


def Total_To_Pay(salary,total_work_days,avance,absence):
    salary = float(salary.replace(",",""))
    day_salary = salary / 30.
    to_pay = (day_salary * float(total_work_days) - float(avance))
    ##print(f"{to_pay:,}")
    return f"{to_pay}"


def Set_Presence(presence):
    connection = sqlite3.connect(f"{DATA_BASE}/gestion_employes.db")
    cursor = connection.cursor()
    try:
        query = f'''
            INSERT INTO LISTE_PRESENCE
            (
                ENTREPRISE_DU_TRAVAIL,
                NUM_EMPLOYE,
                DATE,
                PRESENCE_VALIDE,
                PRESENT,
                TOTAL_TRAVAIL
            )
            VALUES(
                "{presence["entreprise_de_travail"]}",
                "{presence["num_carte_nationale"]}",
                "{TODAY}",
                "NON",
                "NON",
                0.0
            );   
            '''
        cursor.execute(query)
        connection.commit()
    except sqlite3.Error as error:
        return []   
    return


def Update_Presence(username,presence):
    connection = sqlite3.connect(f"{DATA_BASE}/gestion_employes.db")
    cursor = connection.cursor()
    try:
        query = []
        query.append( 
            f'''
                UPDATE "LISTE_PRESENCE"
                SET 
                    PRESENCE_VALIDE = "OUI",
                    PRESENT = "{presence['PRESENCE']}",
                    TOTAL_TRAVAIL = "{presence['TOTAL_TRAVAIL']}"
                WHERE
                    NUM_EMPLOYE = {presence['NUM_EMPLOYE']} 
                    AND
                    ENTREPRISE_DU_TRAVAIL = '{username}';   
            '''
            )
        query.append(
            f'''
                UPDATE "PAYEMENT_EN_COURS"
                SET 
                    PRESENCE_VALIDE = "OUI",
                    PRESENCE_AUJOURDHUI = "{presence['PRESENCE']}"
                WHERE
                    NUM_EMPLOYE = {presence['NUM_EMPLOYE']}
                    AND
                    ENTREPRISE_DU_TRAVAIL = '{username}';
            '''
            )
        for i in range (len(query)):
            count = cursor.execute(query[i])
            connection.commit()
        cursor.close()
        Response = Info_Msg("Succes","Presence faite avec Succes","success")
        return Response

    except sqlite3.Error as error:
        ##print("Failed to update data into sqlite table", error)
        Response = Info_Msg("Erreur","Echec de Faire cette Presence","error")
        return Response    


def Sync_Presence(username):
    connection = sqlite3.connect(f"{DATA_BASE}/gestion_employes.db")
    cursor = connection.cursor()
    try:
        query = []
        query.append(
            f'''
            SELECT
                * 
            FROM "LISTE_PRESENCE"
            WHERE 
                DATE != "{TODAY}"
                AND
                ENTREPRISE_DU_TRAVAIL = "{username}"

            '''
        )
        query.append(
            f'''
            DELETE
            FROM "LISTE_PRESENCE"
            WHERE
                DATE != "{TODAY}"
                AND
                ENTREPRISE_DU_TRAVAIL = "{username}"
            '''
        )
        query.append(
            f'''
            INSERT OR IGNORE INTO "LISTE_PRESENCE"
            (
                ENTREPRISE_DU_TRAVAIL,
                NUM_EMPLOYE,
                DATE,
                PRESENCE_VALIDE,
                PRESENT,
                TOTAL_TRAVAIL
            )
            SELECT 
                ENTREPRISE_DU_TRAVAIL,
                NUM_EMPLOYE,
                "{TODAY}",
                "NON",
                "NON",
                0.0
            FROM
                "PAYEMENT_EN_COURS"
            WHERE
                "ENTREPRISE_DU_TRAVAIL" = "{username}";
            '''
        )
        results = []
        for i in range(len(query)):
            if(i == 0):
                results = cursor.execute(query[i]).fetchall()
                connection.commit()
            else:
                cursor.execute(query[i])
                connection.commit()
        cursor.close()
        return results
        
    except sqlite3.Error as error:
        return []   


def Show_Presence(username):
    
    connection = sqlite3.connect(f"{DATA_BASE}/gestion_employes.db")
    cursor = connection.cursor()
    query = f'''SELECT "LISTE_PRESENCE".NUM_EMPLOYE,
                        "EMPLOYE".NOM,
                        "EMPLOYE".PRENOM,
                        "LISTE_PRESENCE".PRESENCE_VALIDE,
                        "LISTE_PRESENCE".PRESENT,
                        "LISTE_PRESENCE".TOTAL_TRAVAIL
                FROM "EMPLOYE" 
                INNER JOIN "LISTE_PRESENCE" ON "EMPLOYE".NUM_CARTE_NATIONALE = "LISTE_PRESENCE".NUM_EMPLOYE
                INNER JOIN "PAYEMENT_EN_COURS" ON "EMPLOYE".NUM_CARTE_NATIONALE = "PAYEMENT_EN_COURS".NUM_EMPLOYE
                WHERE "LISTE_PRESENCE".ENTREPRISE_DU_TRAVAIL="{username}" 
                    AND "EMPLOYE".DATE_ARRET_TRAVAIL='EN_TRAVAIL';
            '''
    results = connection.execute(query).fetchall()
    connection.commit()
    return results





