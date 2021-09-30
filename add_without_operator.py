def add(a,b):
	if(b==0):
		return a
	else:
		return(a^b,(a&b) << 1)
a=int(input())
b=int(input())

print(add(a,b))
