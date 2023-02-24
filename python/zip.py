#zip function using list
a=[1,2,3,4,5,6]
b=[100,200,300,400,500,600]
c=zip(a,b)
#print(list(c))

#tuples using zip
m=("ooty","coonoor","banglore","coimbatore")
n=("oo","co","ba","coi")
o=zip(m,n)
#print(tuple(o))

for m,n in 0:
    if m < n:
       print("profit:", m-n)
    elif m > n:
        print("loss:",n-m)





