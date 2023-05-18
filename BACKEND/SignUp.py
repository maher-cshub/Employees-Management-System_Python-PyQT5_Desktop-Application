import sqlite3

DATA_BASE = "./BACKEND/data"

def Sign_Up_Admin(username , password):
    Response = {}
    ##try to connect to db
    connection = sqlite3.connect(f"{DATA_BASE}/gestion_employes.db")
    if not connection:
        error_title = "Erreur Conncetion"
        error_text = "Erreur Inatendu a la connection !"
        Response["title"] = error_title
        Response["text"] = error_text
        Response["type"] = "error"
        return Response

    ##connection success          
    query = f"INSERT INTO ENTREPRISE (USER_NAME, PASSWORD) VALUES ('{username}' , '{password}')"
    try:
        connection.execute(query)
        connection.commit()
        Response["title"] = "Success"
        Response["text"] = "Veuillez connecter a votre compte pour commencer"
        Response["type"] = "success"
    except sqlite3.Error as err:
        if(err.__class__ == sqlite3.IntegrityError):
            Response["title"] = "Erreur"
            Response["text"] = "utilisateur deja existe, veuillez utiliser un autre nom utilisateur"
            Response["type"] = "error"
        else:
            Response["title"] = "Erreur Inatendu a la creation de votre compte"
            Response["text"] = "veuillez reessayer la creation de votre compte"
            Response["type"] = "error"
    
    connection.close()
    return Response
