from database_work import create_db
from interface_app import run_interfeis

def init_interf():   
    create_db()
    run_interfeis()
    
if __name__ == "__main__":
    init_interf()