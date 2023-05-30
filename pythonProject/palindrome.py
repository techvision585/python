def program(word):
    rword=word[::-1]
    if rword==word:
        return True
    else:
        return False
word=input("enter the word you wanted to test")

if program(word):
 print("word is palindrom")
else:
 print("word is not palindrom")