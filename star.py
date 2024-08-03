a=1
for i in range(1,6):
    for k in range(6-i):
        print(" ",end="")
    for j in range(1,i+1):
        print(a," ",end="")
        a+=1
    print(" ")
