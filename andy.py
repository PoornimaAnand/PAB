'''
str=input()
rev=str[::-1]
if(rev==str):
	print("palindrome")
else:
	print("not palindrome")
    
#print(str.reversed())
'''
'''
print("Enter number to be reveresed:")
n=int(input())
digi=0
rn=0
while(n!=0):
    digi=n%10
    rn=(rn*10)+digi
    n=n//10
print(rn)
'''
import array
dict={1:"abc",2:"def"}
print(dict)

    
arr=(1,2,3,4)
print(arr)
'''
arr.insert(4,5)
print(arr)
'''

list=[1,2,3,4]
print(list)
list.append(5)
print(list)

set1={"hi",1,2,3,"welcome"}
print(set1)