text = "Hello, welcome to Python! How's everything?"

punct = ".,?!;:'\"-(){}[]"

result = ""

for ch in text:
    if ch not in punct:
        result += ch

print(result)
