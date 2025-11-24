# this is regis.py

rUsers = []

def reg():
    name = input("enter the name here:__")
    password = input("enter the password here:__")
    rUsers.append({"name": name, "pswd": password})
    print("reg successful")
