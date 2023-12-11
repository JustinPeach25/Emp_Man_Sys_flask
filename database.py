from flask import g
from pymongo import MongoClient

def connect_to_database():
    client = MongoClient("mongodb+srv://JustinPeach:justpassword1234@employeemanagement.lfmsmu6.mongodb.net/EmploymentManagement")
    return client.get_database()

def get_db():
    if not hasattr(g, 'application_db'):
        g.application_db = connect_to_database()
    return g.application_db

