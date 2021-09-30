#program to remove duplicates
import array
arr4, count = [],[] 
n = int(input("enter size of array : "))
for x in range(n):
    count.append(0)
    x=int(input("enter element of array : "))
    arr4.append(x)
print("Array elements after removing duplicates")
for x in range(n):
    count[arr4[x]]=count[arr4[x]]+1
    if count[arr4[x]]==1:
        print(arr4[x]) 