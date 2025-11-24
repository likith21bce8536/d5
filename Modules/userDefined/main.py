# this is main.py

from regis import reg
from login import log

while True:
    print("choose below")
    print("1.register")
    print("2.login")

    op = input("enter the option you want: ")

    if op == "1":
        reg()
    elif op == "2":
        log()
    else:
        print("invalid option")



