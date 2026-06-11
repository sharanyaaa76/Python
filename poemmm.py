with open("poem.txt", "r") as f:
    content = f.read()

if "twinkle" in content:
    print("the word twinkle is present in the content")
else:
    print("the word twinkle is not present in the content")
