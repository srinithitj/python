a=[1,2,2,3,44]
y=[]
for i in range(len(a)):
    for j in range(len(a)):
        if i!=j:
            if a[i]==a[j]:
                y.append(a[i])
print(y)
