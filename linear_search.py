arr=list(map(int,input().split()))
b= int(input("Enter the value:"))
count=0
for i in arr:
    if i ==b:
        count+=1
print(count)
