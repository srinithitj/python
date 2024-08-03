n=[1,2,3,4,5,6]
m=[9,8,7,66,55]
y=m[::-1]
print(y)
v=[]
for i in range(len(n)):
    for j in range(len(y)):
        v.append(n[i])
        v.append(y[j])
print(v)
        
