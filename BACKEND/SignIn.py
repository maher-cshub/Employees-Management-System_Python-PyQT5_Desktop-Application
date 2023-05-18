import sqlite3


DATA_BASE = "./BACKEND/data"

def Sign_In_Admin(username , password):
    Response = {}
    ##try to connect to db
    connection = sqlite3.connect(f"{DATA_BASE}/gestion_employes.db")
    if not connection:
        error_title = "Erreur Connection"
        error_text = "Erreur Inatendu a la connection !"
        Response["title"] = error_title
        Response["text"] = error_text
        Response["type"] = "error"
        return Response

    ##connection success          
    query = "SELECT USER_NAME, PASSWORD FROM ENTREPRISE"
    results = connection.execute(query)
    connection.commit()
    user_found = False
    for result in results:
        if(username == result[0] and password == result[1]):
            user_found = True
    if(user_found == True):
        Response["title"] = "Connection Avec Success !"
        Response["text"] = f"Bienvenue {username}, Bonne Journee a Vous !"
        Response["type"] = "success"
        connection.close()
        return Response
    else:
        Response["title"] = "Connection Non Valide !"
        Response["text"] = f" (Ay ya Yay) Vous avez Oublie votre Nom utilisateur ou votre Mot de Passe) !"
        Response["type"] = "error"
        connection.close()
        return Response
    