n=0
u=0
l=0
m=0
while(n!="*"):
    n=input("enter any character: ")
    if n.isupper():
        u+=1
    elif n.isdigit():
        m+=1
    elif n.islower():
        l+=1

print("uppercase: ",u)
print("lowercase: ",l)
print("numbers: ",m)

        
    
