print("---------------Example of diff variable name - Global,Class,Local---------------------------")


g1=10
g2=20
name="Sanky"

class Sample5:
    c1=30
    c2=40

    def m1(self):
        l1=50
        l2=60

        print("Local Variable",l1,l2)
        print("Class Variable",self.c1,self.c2)
        print("Global Variable",g1,g2)               #Global variables are accessible throughout file



s5=Sample5()
s5.m1()

print("---------------Example of same variable name - Global,Class,Local---------------------------")
class Sample6:
    g1=50
    g2=60
    def add(self):
        g1=20
        g2=30
        print("Global Variable Addition",g1+g2)
        print("Class Variable Addition",self.g1+self.g2)
        print("Local Variabl Addition",globals()["g1"]+globals()["g2"])

    @staticmethod
    def sub():

     print("Static Method")
     divide=g1/g2

     print("Dividation in Static Method",divide)


        

s6=Sample6()
s6.add()
Sample6.sub()
