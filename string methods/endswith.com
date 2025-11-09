text="tamil.com"
if text.endswith(".com"):
    print("the ends with '.com'")

else:
    print("the ends doesn't with '.com'")
