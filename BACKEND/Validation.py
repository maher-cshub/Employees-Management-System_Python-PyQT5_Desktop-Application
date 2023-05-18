import re
from datetime import datetime

TODAY =datetime.today().strftime('%d/%m/%Y')

def Isvalid_Password(password):
    regex = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?_&-])[A-Za-z\d@$!#%*?&]{8,20}$"
    pattern = re.compile(regex)
    return re.search(pattern, password)

def Isvalid_Username(username):
    return re.match(r'[A-Za-z0-9_]{4,}',username) and (len(username) >= 4)

def Isvalid_Name(name):
    return re.match(r'[A-Za-z]{3,}',name) and (len(name) >= 3)

def Isvalid_NumCarteNationale(num_carte):
    return re.match(r'[0-9]{18}',num_carte) and (len(num_carte) == 18)

def Isvalide_DateOfBirth(date):
    return((datetime.strptime(TODAY, "%d/%m/%Y") - datetime.strptime(date, "%d/%m/%Y")).days >= 15*365)

def Isvalid_Address(address):
    return re.match(r'[A-Za-z0-9_\s]{5,}',address) and (len(address) >= 5)

def Isvalide_DateOfStartWork(date,date_birth):
    old_enough = (datetime.strptime(date, "%d/%m/%Y") - datetime.strptime(date_birth, "%d/%m/%Y")).days >= 15*365
    less_than_today = (datetime.strptime(date, "%d/%m/%Y") <= datetime.strptime(TODAY, "%d/%m/%Y"))
    return(old_enough and less_than_today)

def Isvalide_DateOfEndWork(date,date_start_wok):
    return((datetime.strptime(date, "%d/%m/%Y") - datetime.strptime(date_start_wok, "%d/%m/%Y")).days > 0)

def Isvalide_Salaire(salaire):
    return (isinstance(salaire,int))

def Isvalide_NumTel(telephone):
    return re.match(r'[0-9]{10}',telephone) and (len(telephone) == 10)

def Isvalid_Obsrevation(observation):
    return re.match(r'[A-Za-z0-9_]{4,}',observation) and (len(observation) >= 4)