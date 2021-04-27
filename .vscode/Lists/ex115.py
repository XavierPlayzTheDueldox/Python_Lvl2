def pig_latin(word):
    word = list(word)
    if word[0] in ['a','e','i','o','u']:
        word.append('way')
    else:
        addlist = list()
        while not word[0] in ['a','e','i','o','u']:
                addlist.append(word[0])
                word.remove(word[0])
        addlist.append('ay')
        word.append(''.join(addlist))
    return ''.join(word)

if __name__ == '__main__':
    inp = input('Enter a string:')
    listofwords = inp.split()
    for i, word in enumerate(listofwords):
        listofwords[i] = pig_latin(word)
    print(' '.join(listofwords))

    