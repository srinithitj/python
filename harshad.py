n=int(input("enter n: "))
m=[int(i) for i in str(n)]
s=0
for i in m:
    s+=i
print(s)
if n%s==0:
    print("harshad")
else:
    print("not harshad")
