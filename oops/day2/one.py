name="likith"
age=21
batch="d5"
edu="it"
class addStudent:
    def __init__(self,n,a,b,e):
        self.stu_name=n
        self.stu_age=a
        self.stu_batch=b
        self.stu_edu=e

    def detailsStu(self):
        print(self.stu_age) 
stuObj=addStudent(name,age,batch,edu)
print(stuObj.stu_name)
stuObj.detailsStu()