a=[1,2,2,3,4,5]
n=len(a)
s=sum(a)
mean=s/n
print("mean: ",mean)
if n%2==0:
    m1=a[n//2]
    m2=a[n//2-1]
    median=(m1+m2)/2
else:
    median=a[n//2]
print("median: ",median)
mode=max(a,key=a.count)
print("mode: ",mode)
 
