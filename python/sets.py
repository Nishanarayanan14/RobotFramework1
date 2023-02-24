#set is a unorderd homogenius
#no dupilicate are allowed
s={10,11,23,8,7,'A'}
print(s)
print(len(s))
print(50 in s)
s.add(100)
print(s)
s.pop()
print(s)
s.pop()
print(s)
s.remove(7)
print(s)

T= {55,57,67,45}
A= {66,77,88}
Z=T.union(A)
print(Z)
B=T.symmetric_difference(A)
print(B)
C={44,34}
print(T.issuperset(C))
C.discard(52)
print(C)


