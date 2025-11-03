a=int(input("enter the age: "))
b=input("do you have experience? (yes/no): ")
if a > 18 and b.lower() == "yes":
    print("eligible.")
else:
    print("you are not a eligible.")
