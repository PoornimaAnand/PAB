
#find missing number from array
arr = []
n = int(input("enter size of array : "))
for x in range(n-1):
    x=int(input("enter element of array : "))
    arr.append(x)
sum = (n*(n+1))/2;
sumArr = 0
for i in range(n-1):
    sumArr = sumArr+arr[i];
print(int(sum-sumArr)) 


#find duplicate element
arr, occur = [], [];
n = int(input("please enter the size of array: "))
for x in range(n):
    occur.append(0)
for x in range(n):
    element = int(input(f"please enter the element of array element between 0 to {n-1} :"))
    arr.append(element)
    occur[arr[x]]=occur[arr[x]]+1
for x in range(n):
    if occur[x]>1:
        print(f"{x} is repeated {occur[x]} times") 
        
#program to compare two array sizes
arr1=[1,2,3,4,5]
arr2=[1,3,4,5,7]
if len(arr1) == len(arr2):
    print("array is equal")
else:
    print("array is not equal") 
    

#find the largest and smallest array element
arr1=[]
large=0
small=0
n=int(input("Enter size"))
for i in range(n):
    ele=int(input())
    arr1.append(ele)
large=arr1[0]
small=arr1[0]
for i in range(n):
    if arr1[i] > large:
        large=arr1[i]
    if (arr1[i]<small):
        small=arr1[i]
print(large)
print(small)

#find second largest number
import array
arr = []
n = int(input("enter size of array : "))
for x in range(n):
    x=int(input("enter element of array : "))
    arr.append(x)
 
sorted_array = sorted(array.array('i', arr))
for i in range(len(arr)-1, 0, -1):
    if sorted_array[i]!=sorted_array[i-1]:
        print(f"second largest element is {sorted_array[i-1]}")
        break 
        
        
#program to find two largest element in an array
import array
arr = []
n = int(input("enter size of array : "))
for x in range(n):
    x=int(input("enter element of array : "))
    arr.append(x)
sorted_array = sorted(array.array('i', arr))
for i in range(len(arr)-1, 0, -1):
    if sorted_array[i]!=sorted_array[i-1]:
        print(f"First two largest element of array is {sorted_array[i-1]} and {sorted_array[i]}")
        break 
        
 
 #program to count pairs
def getPairsCount(arr,n,sum):
    count = 0  # Initialize result
    for i in range(0, n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == sum:
                count += 1
 
    return count
    
arr = [1, 5, 7, -1, 5]
n = len(arr)
sum = 6
print("Count of pairs is",
      getPairsCount(arr, n, sum))
 
 
# Driver function
arr = [1, 5, 7, -1, 5]
n = len(arr)
sum = 6
print("Count of pairs is",
      getPairsCount(arr, n, sum))
 
 
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