#Ex 116 Pig Latin Improved
from ex115 import pig_latin

#reading n splitting
inp = list(input('Enter a string:'))

#Tracks Data of punctuation
upper, punc = None, list()
if not inp[-1].isalpha():
    punc.append(inp[-1])
    inp.pop(-1)
    
if inp[0].isupper():
    upper = True
    inp[0] = inp[0].lower()

listofwords = ''.join(inp).split()

#translates all word to pig latin ONLY
for i, word in enumerate(listofwords):
    listofwords[i] = pig_latin(word)

#Repunctuates sentence
listofwords.append(''.join(punc))
if upper == True:
    listofwords = list(''.join(listofwords))
    listofwords[0] = listofwords[0].upper()
    listofwords = ''.join(listofwords)

print(' '.join(listofwords))