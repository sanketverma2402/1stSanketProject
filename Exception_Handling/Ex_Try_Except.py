

class Exception:

    def m1(self):
        print("---------------Program Started---------------")
        a=10
        b=0

        print("-----Ex1.1: basic example of Exception handling------")
        try :
            c=a/b
            print(c)               # 10/0  = error          #risky code
        except BaseException :   #Note--Yes, BaseException can handle any type of error in Python — but it should rarely be used directly in most cases.
                                #Or else provide exception shown in output
            print("ZeroDivision Error Handled : Division byZero Is Not Allowed In Python")

        print("---------------Program Ended---------------")

    def m2(self):
        print("---------------Program Started---------------")
        print("-----1.2: basic example of Exception handling -> With Alternate code------")
        a=20
        b=0
        try:
            print(a/b)              #Risky Code should be in try block always
        except ZeroDivisionError:
            print(a/1, "Exception Handled With Alternative Code")

        print("---------------Program Ended---------------")

    def m3(self):
        print("---------------Program Started---------------")
        a=30
        b=0
        print("-----2: Multiple Except block for 1 try block------")
        try :
            print(a/b)

        except ValueError:
            print("ValueError Handled")
        except ZeroDivisionError:
            print("ZeroDivisionError Handled ")   #It will find Except block for correct error and does not give error

        except AssertionError:
            print("AssertionError Handled")


        print("---------------Program Ended---------------")

    # def m4(self):
    #     # print("-----Ex3: Generic Exception------")
    #     # print("Program started")
    #     # a = 10
    #     # b = 0
    #     # try:
    #     #     print(a / b)  # risky code
    #     # except Exception as e:                  #Not Working
    #     #     print(e)
    #     #     print("Generic Exception Handled")
    #     #
    #     # print("Program ended")

    def m5(self):
        print("-----Ex4: Correct way of using Generic Exception------")
        print("Program started")
        try:
            result = 10 / 0
        except :
            print("Exception Handled")                 

        print("Program ended")


e1=Exception()
e1.m1()
e1.m2()
e1.m3()
#e1.m4()
e1.m5()