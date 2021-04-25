word = input('Enter a string:')
neg_check = len(word) - 1 
pos_check = 0
num_check = 0
while word[neg_check] == word[pos_check] and neg_check > pos_check:
    neg_check -= 1
    pos_check += 1
    num_check += 1
    
if num_check == len(word) // 2:
    print('Your string is a Palindrome.')
else:
    print('Your string is not a Palindrome.')