n=int(input())
sum=0
dig=0
temp=0
temp=n
while(temp>0):
	dig=temp%10
	sum=sum+dig**3
	temp=temp//10
if sum==n:
	print("Armstron")
else:
	print("Not armstrong")