#formating the string
a="my name is nisha"
b="how are you"
print("welcome"+a)
print("welcome",a,b)
print("welcome{}{}".format(a,b))
print("welcome{a}{b}".format(a,b))
print("welcome{about}{question}".format(about=a,question=b))