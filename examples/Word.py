my_string = "Hello this is trailer of Samreach's code"

words = [word.lower() for word in my_string.split()]

print("=> Splited words : ")
for word in words:
    print(word)

words.sort()
print("=> Sorted words :")
for word in words:
    print(word)