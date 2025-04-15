class Demo:

    def __init__(self):
        print("Constructor without parameter or variable")
    def m1(self):
        print("Timepass Method")


c1=Demo()                  #Constructor Call Only

print("---------------------------------------------------------------------------")
class Demo2:

    def __init__(self,num3,num4):
        num1=10
        num2=20
        self.a=num3                                  #Initializing parameter variable to Self variable
        self.b=num4

        print("Constructor with parameter or variable")
        print("Add Output",num1+num2)


    def mult(self):
        m=self.a*self.b
        print("Mult Output",m)              #Accessing Constructor variable in Method using Self

    def sub(self):
        s=self.a-self.b
        print("sub Output",s)              #Accessing Constructor variable in Method using Self

    def div(self):
        d=self.a/self.b
        print("Div Output",d)              #Accessing Constructor variable in Method using Self

d2=Demo2(5,2)
d2.mult()
d2.sub()
d2.div()
