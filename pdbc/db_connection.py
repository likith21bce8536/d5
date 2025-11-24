import mysql.connector

def db_connection_func():
    return mysql.connector.connect(
    host="localhost",
    user="root",
    database="drivedb",
    password ="Likith123$"
)