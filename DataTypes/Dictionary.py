employee={
    "name":"Sanket Verma",
    "age":28,
    "empId":126009,
    "avg":0.9,
    "Is-Employed":True,
    "CoursesDone":["Python","Selenium","Java"],
    "CoursesNotDone":("Cucumber","aws"),
    "Languages":{"Hindi","Eng","Marathi"}
}

print(type(employee))
print("----------------------------------")
print(employee.keys())
print("----------------------------------")
print(employee.values())
print("----------------------------------")
print(employee.items())
print("----------------------------------")
print(employee.get("age"))
print("----------------------------------")
print(employee.get("CoursesDone"))
print("----------------------------------")
employee.pop("Languages")
print(employee)
print("----------------------------------")
employee["salary"]=30000
print(employee)
print("----------------------------------")
employee["salary"]=40000
print(employee)
print("----------------------------------")
print(employee.__contains__("salary"))
print("----------------------------------")
for key,value in employee.items():
    print(key,"=",value)

print("-------------------------------------------")
#--------Create Dictionary dynamically a run time----------
dict1={}
dict1["firstname"]="abc"
dict1["lastname"]="xyz"
dict1["Gender"]="male"
print(dict1)
print("FN: "+dict1["firstname"])