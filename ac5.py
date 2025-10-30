# Apna college Python lecture 5
# loops
count=1
while count<=1008:
    print(count)
    count = count+1

n=int(input("Enter the number:"))
count=1
while count<=10:
    Ans=n*count
    print(Ans)
    count=count+1

nums=[1,4,9,16,25,36,49,64,81,100]
index=0
while index<len(nums):
    print(nums[index])
    index=index+1

nums=(1,4,9,16,25,36,49,64,81,100)
key=25
i=0
while i<len(nums):
    if(nums[i]==key):
        print("Found")
        break
    else:
        print("Not found") 
    i+=1 

n=7
sum=0
for i in range(1,n+1):
    sum=sum+i
print(sum)
