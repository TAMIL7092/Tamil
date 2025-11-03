a=int(input("enter the year:"))
if a%400==0:
    print(a,"is a leap year")    
elif a%100==0:
    print(a,"This is not a leap year")
elif a%4==0:
    print(a,"is a leap year")
    
else:
    print("This is not a leap year")
