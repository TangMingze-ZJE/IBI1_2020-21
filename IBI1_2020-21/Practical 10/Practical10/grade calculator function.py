class grade_caculator:
    def _init_(self,sn,cg,pg,fg):
        self._sn=sn
        self._cg=cg
        self._pg=pg
        self._fg=fg

def getgrade(self):
    grade = self._cg*0.4 + self._fg*0.3 + self._pg*0.3
    return round(grade*100)/100

def getname(self):
    return self._sn
student1=grade_caculator('John',78,99,79)
print(student1.getnam(),'total grade is',student1.getgrade())
a=input('Your name is:')
b=input('your code portfolio grade is:')
c=input('your poster presentation grade is:')
d=input('your final exam grade is:')

student2 = grade_caculator(a,int(b),int(c),int(d))
print(student2.getname(),'total grade is',student2.getgrade())
