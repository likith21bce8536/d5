from admin_features import add_student,get_student,update_student,delete_student,add_task,class_recordings
def admin():
    print("you are in admin panel")
    print("choose yr opeartion to proceed with ")
    print("1. add student")
    print("2. get student")
    print("3. update student")
    print("4. delete student")
    print("5. addd task")
    print("6. addd  recordings")


    op=int(input("enter yr choice here :--  "))
    if op == 1:
        add_student()
    if op==2:
        get_student()
    if op == 3:
        update_student()
    if op==4:
        delete_student()  
    if op==5:
        add_task()
    if op==6:
        class_recordings()