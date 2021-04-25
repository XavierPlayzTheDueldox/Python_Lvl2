punctuations = list('''!()-[]}{;:'"\,<>./?@#$%^&*_~'''' ')

word = input('Enter a string:')
word = str.lower(word)
number = word.count(' ')
no_punct = ""
for r in word:
   if r not in punctuations:
       no_punct = no_punct + r

neg_check = len(no_punct) - 1 
pos_check = 0
num_check = 0
while no_punct[neg_check] == no_punct[pos_check] and neg_check > pos_check:
    neg_check -= 1
    pos_check += 1
    num_check += 1
    
if num_check == len(no_punct) // 2:
    print('Your string is a Palindrome.')
else:
    print('Your string is not a Palindrome.')




