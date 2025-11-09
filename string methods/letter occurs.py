text = "hello python"

count = {}

for ch in text:
    if ch.isalpha():
        if ch in count:
            count[ch] += 1
        else:
            count[ch] = 1

print(count)
