a=input("enter string: ")
vow=0
cons=0
s=0
v="aeiouAEIOU"
for i in a:
    if i in v:
        vow+=1
    elif i.isspace():
        s+=1
    else:
        cons+=1
print("no of vowels: ",vow)
print("no of consonants: ",cons)
if vow>cons:
    print("vowels is max")
else:
    print("consonants is maximum")
