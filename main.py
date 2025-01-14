from database import create_db
from interfeis_app import run_interfeis

def init_interf():   
    create_db()
    run_interfeis()
    
if __name__ == "__main__":
    init_interf()