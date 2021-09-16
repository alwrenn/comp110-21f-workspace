"""Finding duplicate letters in a word."""

__author__ = "730384411"

word: str = str(input("Enter a word: "))
length: int = len(word)
counter: int = 0
a: int = 0


while a < length:
    b: int = 0
    while b < length: 
        if word[a] == word[b] and a != b:
            counter += 1
        b = b + 1
    a = a + 1
if counter >= 1:
    print("Found duplicate: True")
else:
    print("Found duplicate: False")
        

      