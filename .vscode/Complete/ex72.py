word = input('Enter your string:')
rev_word = reversed(word)

if list(word) == list(rev_word):
   print("The string is a palindrome.")
else:
   print("The string is not a palindrome.")
        