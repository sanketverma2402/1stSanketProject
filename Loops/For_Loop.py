print("---------table of 7-----------")
for i in range(1,11):
    print(str(i*7)+",")

print("---------print square of num from 5 to 10-----------")
for i in range(5,11):
    print(i*i)

#####Example5:

print("---------print Even num from 10 to 2----------")
#startNum=10
#end num=2
#incr/decr= decr num by 2

for i in range(10, 1,-2):   #10-2=8-2=6-2=4-2=2-2=0    0>1 -> true/false  starNum>endNum
    print(i)            #10 8 6 4 2


print("---------print Even num from 100 to 20----------")
for i in range(13, 100):
    print(i)




####Example6:

studentAllData=["Amol", 101, 65.1,'A']

print("------Print all data from list------")
for singleData in studentAllData:
    print(singleData)


print("------Print all data from list in Reversed order------")
for singleData in reversed(studentAllData):
    print(singleData)
