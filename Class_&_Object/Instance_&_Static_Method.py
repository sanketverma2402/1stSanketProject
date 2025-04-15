class Sample2:

    def m1(self):
        print("Running Instance Method")

    @staticmethod
    def m2():
        print("Running Static Method")


s1=Sample2()
s1.m1()
Sample2.m2()
