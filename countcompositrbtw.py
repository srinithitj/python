n=int(input("enter n: "))
m=int(input("enter m: "))
v=[]
if n>m:
    t=n
    n=m
    m=t
for i in range(n+1,m):
    for j in range(2,i):
        if i%j==0:
            if i not in v:
                v.append(i)
print(v)
