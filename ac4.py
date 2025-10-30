# Apna college Python Lecture 4
# Dictionary and their methods
student={
    "name":"Atul Kumar",
    "subjects":{
        "phy":97,
        "chem":98,
        "math":95
    }
}
student.update({"name":"Atul Pal"})
print(student)

# Sets and their methods
set={1,2,3,4}
print (set)
print(type(set))

set1={1,2,3,4}
set2={3,4,5,6}
print(set1.union(set2))
print(set1.intersection(set2))

# lets practice 
dict={
    "table":["A peice of furniture","list of facts and figeures"],
    "cat":"a small animal"
}
print (dict)

subjects={"python","java","c++","python","javascript","java","python","java","c++","c"}
print(subjects)
print("No. of classrom needed:",len(subjects))

dict={}
x=int(input("Enter the marks of maths:"))
dict.update({"math":x})
y=int(input("Enter the marks of phy:"))
dict.update({"phy":y})
z=int(input("Enter the marks of chem:"))
dict.update({"chem":z})
print(dict)