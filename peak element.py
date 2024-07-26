a=[1,2,4,3]
even=[]
odd=[]
for i in a:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print("odd: ",odd)
print("even:",even)
person={"name":"jeethu","age":22,"gender":"male","city":"chennai"}
print(person)
n = 3025
m = str(n)
a = m[:len(m)//2]
b = m[len(m)//2:]
c = int(a)+int(b)
d = c**2
if(d==n):
   print("Tech number")
else:
   print("Not a Tech number")
