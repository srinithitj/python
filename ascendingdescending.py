n=input("enter : ")
m=input("enter (A/D/B): ")
s=str(n)
a=sorted(s)
b=a[::-1]
d="".join(a)
c="".join(b)
if m=="A":
    print("ascending order = ",d)
elif m=="D":
    print("descending order = ",c)
elif m=="B":
    print("ascending order = ",d)
    print("descending order = ",c)
