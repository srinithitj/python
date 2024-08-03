n=[1,2,3,4,5,6,7,8,9]
p=[]
c=[]
for i in n:
    if i>0:
        is_prime=True
    for j in range(2,i):
        if i%j==0:
            is_prime=False
    if is_prime:
        if i not in c:
            p.append(i)
    else:
        if i not in p:
            c.append(i)
print("prime: ",p)
print("composite: ",c)
