p=int(input("enter physics mark: "))
m=int(input("enter maths mark: "))
c=int(input("enter chemistry mark: "))
avg=(p+m+c)/3
if (avg>=90):
    print("grade : A")
elif (avg<90) and (avg>=80):
    print("grade : B")
elif (avg<80) and (avg>=70):
    print("grade : C")
elif (avg<70)and (avg>=50):
    print("grade : D")
else:
    print("grade : F")
