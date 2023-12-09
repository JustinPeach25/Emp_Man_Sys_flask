from flask import g
import sqlite3

def connect_to_database():
    sql = sqlite3.connect('C:/Users/peach/OneDrive/Desktop/Emp_Man_Sys_flask/application.db')
    sql.row_factory = sqlite3.Row
    return sql

def get_db():
    if not hasattr(g, 'application_db'): 
        g.application_db = connect_to_database()

        return g.application_db  
