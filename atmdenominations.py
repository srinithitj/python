n=0
m=0
sum=0
for i in range(1,5):
    n=int(input(f"enter {i}st denomination: "))
    m=int(input("enter number of notes: "))
    sum+=n*m
print(sum)
