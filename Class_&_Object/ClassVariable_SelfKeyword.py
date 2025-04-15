class Sample4:
    num1=10
    num2=20
    num3=30

    def add(self):
        a=self.num1+self.num2+self.num3
        print("Addition of Numbers",a)

    def mul(self):
        num4 = 5
        a=self.num1*self.num2*self.num3*num4
        print("Multiplication of Numbers", a)

    def sub(self,num5):

        a=self.num1-self.num2-self.num3-num5
        print("Substraction of Numbers", a)

s1=Sample4()
s1.add()
s1.mul()
s1.sub(5)