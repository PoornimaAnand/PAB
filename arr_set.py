import array
a = [1,2,3]
print(a[-3])

names=['chris','jack','john','daman']
print(names[-1][-5])

#set is an unordered collection of unique elements which are immutable
s = {"hi","welcome","to","world","of","python","hi"}#note hi is repeated 2 times, no error message but it doesnt count as well
print(s)
print(len(s))

s.add("hello")#doesnt work. u cant add elements to set as its immutable


names1 = ['Amir', 'Bear', 'Charlton', 'Daman']
names2 = names1
names3 = names1[:]

print(names1)
print(names2)
print(names3)

names2[0]='Alice'
names3[0]='Bob'
print("")
print(names1)
print(names2)
print(names3)