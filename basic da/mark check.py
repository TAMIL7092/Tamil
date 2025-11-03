a=int(input("Enter the mark"))
b=int(input("Enter the mark"))
c=int(input("Enter the mark"))
avg=(a+b+c)/3
if a>40 and b>40 and c>40:
    print("pass")   
    if avg>=90:
        print("outstanding")
else:
    print("fail")
