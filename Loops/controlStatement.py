print("--------------------For Loop Example-----------------------")

studentData=["Sanky","NT",95.01,'A',40,20,10]

for i in studentData:
    print(i)
    if i=='A':
        break

print("--------------------While Loop Example-----------------------")

evenNums=[0,2,4,6,8,10,12,14,16,18,20]
index=0


while index < len(evenNums):
    print(evenNums[index])
    index=index+1
    if evenNums[index]==10:
        break


