a=[5,4,3,21,2]
v=[]
min=a[0]
for i in range(1,len(a)):
    if min>a[i]:
        v.append(min)
        min=a[i]
print(v)        
    
 
