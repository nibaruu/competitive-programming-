text=input().lower()
table=str.maketrans({
    "a": "",
    "e": "",
    "i": "",
    "o": "",
    "u": "",
})
text="."+".".join(text.translate(table))
print(text)
