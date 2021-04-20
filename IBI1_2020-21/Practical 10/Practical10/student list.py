class Student:
    def _init_(self,name,lastname,course):
        self.name=name
        self.l=lastname
        self.c=course

#定义内部函数实现功能
def getname(self):
    return self.name
def getlastname(self):
    return self.l
def getcourse(self):
    return self.c

student1 = student_list('Mark','Brown','BMS')
print('The example: His/her name is' ,student1.getname(),student1.getlastname(),'and his/her major is',student1.getcourse())

student2=student_list(input('First name is:'),input('Last name is:'),input('The major is:'))
print('His/her name is',student2.getname(),student2.getlastname(),'and his/her major is', student.getcourse())
