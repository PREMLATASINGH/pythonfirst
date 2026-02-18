for i in range(5):
    print(i)
for i in range(1, 10, 3):
    print(i)
for i in  range(10, 0, -2):
    print(i)
str1="Hello"
for i in str1:
    print(i)
count=0
while count<5:
    print(count)
    count+=1
count=0
while count%2==0:   
    print(count)
    count+=1   
count=0
while count<10:
    if count%2==0:
        print(count)
    count+=1
for i in range(10):
    if i==6:
        break                       
    print(i)
for i in range(10):
    if i==6:
        continue                    
    print(i)
for i in range(3):
    for j in range(2):
        print(i,j)
n=10
sum=0
count=1
while count<=n:
    sum+=count
    count+=1    
print(sum)
for i in range(10):
    sum=sum+i  
print(sum)