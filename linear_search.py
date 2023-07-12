arr=list(map(int,input().split()))
b= int(input("Enter the value:"))
def count_num(arr,b):
    count=0
    for i in arr:
        if i ==b:
            count+=1
    return count
print(count_num(arr,b)
