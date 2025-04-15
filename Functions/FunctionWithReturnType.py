#Functions Without Parameter

def name1():
    print("Function Without Parameter")
name1()

print("------------------------------------------------")

#Function With Parameter

def add():
    a,b,c=10,20,30
    add=a+b+c
    print("Addition Function "+"-- "+str(add))

def mul(num1,num2,num3):
    mult=num1*num2*num3
    print("Multiplication Function","--",mult)

add()
mul(10,20,30)


print("------------------------------------------------")

print("--------Ex5: Positional parameter: ---------")
def greet(name, age):
    print("My Name is: ",name)
    print("My Age is: ", age)

# Calling the function with positional arguments
greet("abc", 25)  # Correct order
greet(25, "Alice")  # Incorrect order, meaning changes


print("------Ex6: Keyword parameter(Order/position doesn't matter)------")
def greet(name, age):
    print("My Name is: ",name)
    print("My Age is: ", age)

# Calling the function using keyword arguments
greet(name="xyz1", age=25)
greet(age=30, name="xyz2")  # Order doesn't matter


print("------Ex7: Default/optional parameter------")
def greet(name="abc", age=10):          #providing default vaules to the variables
    print("My Name is: ",name)
    print("My Age is: ", age)

greet()
print("---")
greet("xyz",20)

print("------Function Example With ReturnType------")

def calci(num1):
    square=num1*num1
    return square

print("Printing with ReturnType",calci(5))

squareNum=calci(6)
print("Printing with ReturnType using object",squareNum)