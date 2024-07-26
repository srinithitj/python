a=[1,2,2,3,4,5,6,7,7]
y=[]
for i in range(len(a)):
    for j in range(len(a)):
        if i!=j:
            if a[i]==a[j]:
                y.append(a[i])
print(y)
     
