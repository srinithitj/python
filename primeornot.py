n=int(input("enter n:"))
flag=0
for i in range(2,n):
    if n%i==0:
        print("non prime")
        break
else:
    print("prime")
