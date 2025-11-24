from db_connection import db_connection_func
a=db_connection_func()
print(a,"line 3")
curObj=a.cursor() # you need to have it
print("you are in adminfeatures file where you have all admin features like adding, updating etc..")

def add_task():

    print("you are using task add feature")
    task_id=int(input("enter the task_id"))
    task_topic=input("enter the task topic :--- ")
    task_doc=input("enter the doc link")
    task_issued_date=input("enter the date ")
    query="insert into task2 (task_id,task_topic,task_doc,task_issued_date) values (%s,%s,%s,%s)"
    curObj.execute(query,(task_id,task_topic,task_doc,task_issued_date))
    a.commit()
    print("task is uploaded successfully.......")


def class_recordings():
    print("you are using recording feature")
    reco_id =int(input("enter the recording id"))
    reco_topic=input("enter the recording topic")
    reco_link=input("enter the recording link")
    query="insert into recording (reco_id,reco_topic,reco_link) values (%s,%s,%s)"
    curObj.execute(query,(reco_id,reco_topic,reco_link))
    a.commit()
    print("recording uploaded successfully.......")



def delete_student():
    print("you are using deleting student feature")
    s_id=int(input("enter stude id here to update his details ....   "))
    query="delete from students where stu_admNo=%s"
    curObj.execute(query,(s_id,))
    a.commit()
    print("student data deleted successfully.........")

def update_student():
    print("you are using updating student feature")
    s_id=int(input("enter stude id here to update his details ....   "))
    s_y=int(input("enter st year to be updated ..."))
    query="update students set stu_year=%s where stu_admNo=%s"
    curObj.execute(query,(s_y,s_id))
    a.commit()
    print("student data updated successfully.........")

def get_student():
    print("you are using getting student feature")
    print("you want all students r only few based on criteria")
    op=input("enter all r few")
    if op == "all":
        query="select * from students"
        curObj.execute(query) # getting data
        allStuData=curObj.fetchall()
    else:
        criteria=int(input("enter year of student"))
        criteria2=input("enter dept of students")
        query="select * from students where stu_year=%s and stu_dept=%s"
        curObj.execute(query,(criteria,criteria2))
        few=curObj.fetchall()
        print(few,"few")


def add_student():
    s_adNo=int(input("enetr student id here :---- "))
    s_name=input("enter student name here :-- ")
    s_age=int(input("enter student age here :--- "))
    s_year=int(input("enter which year stidents is"))
    s_dept=input("enter student dept here ")
    
    # query="insert into students (stu_admNo,stu_name,stu_age,stu_year,stu_dept) values (%s,%s,%s,%s,%s)"
    curObj.execute("insert into students (stu_admNo,stu_name,stu_age,stu_year,stu_dept) values (%s,%s,%s,%s,%s)",(s_adNo,s_name,s_age,s_year,s_dept)) # it will execute yr sql query
    # insert, update, delte from python to db :-- commit()
    a.commit()
    print("addedd succesfuly to db")