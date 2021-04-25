def word_extract(resp):
    newlist = list()
    o=0
    while not resp[o+1].isupper() or not resp[o+1].islower():
        for o in resp:
            resp.pop(resp[0])
    for i in resp:
        if resp[i] == ' ':
            newlist.append(resp[0:i])
            resp.pop(resp[0:i])
    return newlist

print(word_extract(list(input('Enter a string:'))))
