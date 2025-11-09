text=input("enter the string")
if len(text)==1:
    result=text.upper()
else:
    first=text[0].upper()
    middle=text[1:-1]
    last=text[-1].upper()
    result=first+middle+last
    print("modified string:",result)
