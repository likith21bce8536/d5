from admin import admin


print("db connected successfully   ........")
print(" choose yr role to proceeed :--  ")
print("1. admin")
print("2. student")

op=int(input("enter yr role here by typing 1 r 2 :----   ")) # 2

if op == 1:
    print("you are as admin")
    admin()
if op ==2:
    print("you are as student")
    student()