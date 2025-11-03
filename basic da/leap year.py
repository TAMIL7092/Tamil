a=int(input("enter the year"))
if a%400==0:
    print("leap year")
elif a%100==0:
    print("not a leap year")
elif a%4==0:
    print("leap year")
else:
    print("not a leap year")
