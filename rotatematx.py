m=[[2,1,3],[2,6,7],[9,8,7]]
for i in range(len(m)):
    for j in range(len(m)):
        m[i][j]=m[j][i]
for i in m:
    print(i)
