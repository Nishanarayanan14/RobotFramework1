#it is heterogenious,ordered,imutable
#tupple is declaried in a () brackets
a=(1,2,5,8,'A','B',5,2)    #TUPPLE DECLARACTION
print(a)
print('A' in a )    #to check whether 'A' is in a or not
print(a[3])         #to check paticular index value
#method in tupple
#count
print(a.count(5))
for i in a:
    print(i,end='')

print(type(a))
b=(2,4,5,7)
z=a+b
print(z)
print(b*3)