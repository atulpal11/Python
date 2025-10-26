str1="Atul "
str2="Pal"
final_str=(str1+str2)
print(final_str)
print(len(final_str))
str="123456789"
print(str[3:-2])

#String Functions
str="i am coder"
print(str.endswith("er"))   #True
print(str.capitalize())    #I am coder
print(str)  #i am coder
str=str.capitalize()
print(str)  #I am coder
print(str)  #I am coder
str1="I will be a great engineer"
print(str1.replace("e","o"))

#Conditional Statements
age=17 
if(age>=18):
    print("You can vote.")
else:
    print("You cannot vote.")

num=int(input("Enter the number:"))
if(num%2==0):
    print("The number entered is even.")
else:
    print("The number entered is odd.")

num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
num3=int(input("Enter the third number:"))
if(num1>num2):
    if(num1>num3):
        print("The first number is greater.")
    else:
        print("The third number is greater.")
elif(num2>num3):
    print("The second number is greater.")
else:
    print("The third number is greater.")
num=int(input("Enter the number:"))
if(num%7==0):
    print("The number is multiple of 7.")
else:
    print("The number is not multiple of 7.")