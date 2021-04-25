def capitalize(sentence):
    check = 0
    pastpunc = True
    while check != len(sentence):
        if check <= len(sentence)-3:
            if pastpunc == True and sentence[check].islower() and sentence[check] != ' ':
                sentence[check] = sentence[check].upper()
                pastpunc = False
            if sentence[check] == '!' or sentence[check] == '.' or sentence[check] == '?':
                pastpunc = True
            if sentence[check] == ' ' and sentence[check+1] == 'i' and sentence[check+2] == ' ' or sentence[check+2] == '':
                sentence[check+1] = sentence[check+1].upper()
            if sentence[len(sentence)-2] == ' ' and sentence[len(sentence)-1] == 'i':
                sentence[len(sentence)-1] = sentence[len(sentence)-1].upper()
        check+=1
    return ''.join(sentence)

sentence = list(input('Enter your Sentence:'))
print(capitalize(sentence))