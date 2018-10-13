import string
word = input()
if len(word)==1:
    word = word.swapcase()
else:
    if  word[1:].isupper() == True:
        word = word.swapcase()


print(word)
