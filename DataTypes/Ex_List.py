ls=[10,20,30,"abc",'A',0.50,40]           #idex starts from 0

print(ls)

print("------------------Print all data from List---------------------")
for i in ls:
    print(i)

print("------------------------")
#find length of list
print(len(ls))                         #length is not index

print("------------------------")
#get data from specific index
print(ls[4])
print(type(ls[4]))

#verify any specific data available in list
print(ls.__contains__(0.50))

#add element
ls.append(50)
print(ls)

#add multiple element
ls.extend([60,70,"xyz"])
print(ls)

#add element to specific object
ls.insert(2,3)
print(ls)

#remove element by index
ls.pop(2)
print(ls)

ls.pop()    #it will remove element from last index
print(ls)

#to remove any object from list
ls.remove(0.50)
print(ls)

#copy list
ls1=ls.copy()
print(ls1)

print("------------sorting-------------")
ls2=[2,4,1,5,3]

#Ascending order
ls2.sort()
print(ls2)

#Descending order
ls2.reverse()
print(ls2)

#Sort list without changing original data
#returns new list without modifying # original list
ls3=sorted(ls2)
print(ls3)

# Searching & Counting
ls4=[1,3,4,6,7,9,4,6,3,1,2,4]
print(ls4.index(3))            # returns 1st occu


print(ls4.count(4))
#clear list
#ls4.clear()
#print(ls4)

#delete list
del ls4
print(ls4)


