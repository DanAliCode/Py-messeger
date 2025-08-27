# Importando biblioteca
from unidecode import unidecode
from pathlib import Path
import pickle

# Files Managers ====================================================
messeger_foulders = Path(__file__).parent / 'mensagens'
messeger_foulders.mkdir(exist_ok=True)
user_foulders = Path(__file__).parent / 'users'
user_foulders.mkdir(exist_ok=True)
timer_rerun = 3

def read_messeger_storage(user1,user2):
    file_name = file_name_storage(user1,user2)
    
    if (messeger_foulders / file_name).exists():
        with open(messeger_foulders / file_name, "rb") as f:
            return pickle.load(f)
    else:
        return []


def messeger_storage(user1,user2,messeger):
    file_name = file_name_storage(user1,user2) 

    with open(messeger_foulders / file_name, "wb") as f:
            pickle.dump(messeger, f)
        
        
        
def file_name_storage(user1,user2):
    file_name = [user1,user2]
    file_name.sort()
    file_name = [u.replace(' ','_') for u in file_name]
    file_name = [unidecode(u) for u in file_name]
    return '&'.join(file_name)

def save_new_user(user,password):
    filename = unidecode(user.replace(" ", "_").lower())
    
    if (user_foulders / filename).exists():
        return False
    else:
        with open(user_foulders / filename, 'wb') as f:
            pickle.dump({'username': user, 'password': password}, f)
        return True   
            
def authenticator_password(user,password):
    filename = unidecode(user.replace(" ", "_").lower())
    if not (user_foulders / filename).exists():
        return False
    else:
        with open(user_foulders / filename, 'rb') as f:
            filepassword = pickle.load(f)
            
        if filepassword['password'] == password:
            return True
        else:
            return False
        

def user_list():
    users = list(user_foulders.glob('*'))
    users = [u.stem.upper() for u in users]
    return users
