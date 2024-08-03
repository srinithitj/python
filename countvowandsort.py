n=input("enter string: ")
v="aeiouAEIOU"
vow=[]
con=[]
for i in n:
    if i in v:
        vow.append(i)
    else:
        con.append(i)
j=",".join(sorted(vow))
k=",".join(sorted(con))

print(j)
print(k)
        
    
