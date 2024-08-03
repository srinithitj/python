n=int(input("enter n: "))
s=""
while(n>0):
    r=n%2
    s=str(r)+s
    n=n//2
print(s)
m=input("enter : ")
decimal=0
power=0
for i in reversed(m):
    decimal+=int(i)*(2**power)
    power+=1
print(decimal)
    
`
