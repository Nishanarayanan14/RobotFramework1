#dictionary
a={"url1":"google.com","url2":"amazon.com"}
b={1:"nisha",2:"akash",3:"moolyaed"}
print(b[1])
print(a["url2"])
print(a["url1"])
b[4]="flipkart.com"
print(b)
print(b[4])
print(b.get(1)) #get method
print(b.keys())
print(b.items()) #values come with form of tupples
print(b.values()) #values
print(b.pop(1)) #enterd key or value will be removed
print(b.keys())
print(b.popitem()) #last element will be deleted
print(b.keys())
b.update({3:"myntra.com",4:"orangehrm.com"})
print(b)
b.clear()  #empty dictionary , it is used to clear the values
print(b)
b.setdefault(5,"youtube.com") #it is used to update the keys or values
print(b)