a=[1,2,3,4,2,3,5,2]
n=int(input("enter the element to count its occurance:"))
count=0
for i in a:
    if n==i:
        count+=1
print(count)
