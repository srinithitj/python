a= [[1,2], [4,1]]
b= [[5,6], [7,8]]
res= [[0,0], [0,0]]
for i in range(len(a)):
    for j in range (len(b)):
        for k in range (len(res)):
         res[i][j]+=a[i][k]*b[k][j]
print ("product matrix:", res)
