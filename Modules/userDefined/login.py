# login.py

from regis import rUsers
from dashboard import dashboard__

def log():
    e = input("enter the name:__")
    p = input("enter the password:__")

    for ruser in rUsers:
        if e == ruser["name"] and p == ruser["pswd"]:
            print("successfully logged in")
        dashboard__(e)     
