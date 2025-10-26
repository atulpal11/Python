#Apna college Python Lecture 3

#List
list=[5,6,1,3,4,9,2]
list.sort()
list.append(7)
list.extend([8])
list.sort()
list.pop(6)
list[3]=3
print(list)

#Q1
element1=str(input("Enter the first movie name:"))
element2=str(input("Enter the second movie name:"))
element3=str(input("Enter the third movie name:"))
list=[]
list.append(element1)
list.append(element2)
list.append(element3)
print(list)

#Q2
a=[1,2,1]
b=a.copy()
b.reverse()
if(a==b):
    print("The elements are pelendrome.")
else:
    print("The elements are not pelendrome.")

#Q3
tup=("C","D","A","A","B","B","A")
print(tup.count("A"))

#Q4
list=["C","D","A","A","B","B","A"]
list.sort()
print(list)