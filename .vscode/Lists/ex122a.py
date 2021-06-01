#def tokenize(new):
    #new = new.replace(' ', '')
    #new = list(new)
    #tokenized= list()
    #add = ''
    #while len(new) != 0:
        #if new[0].isdigit() or new[0] == ('(' or ')' or '*' or '/' or '='):
            #tokenized.append(new[0])
            #new.pop(0)
        #else:
            #if new[1].isdigit():
                #add+=new[0]
                #add+=new[1]
                #tokenized.append(add)
                #for i in range(2):
                    #new.pop(0)
            #else:
                #tokenized.append(new[0])
                #new.pop(0)
    #return tokenized

def tokenize(new):
    new = new.replace(' ', '')
    tokenlist = []
    i = 0
    operatorlist = ['*','/','+','-','^']
    while i < len(new):

        if new[i] in operatorlist:
            tokenlist.append(new[i])
            i+= 1

        elif new[i] == "+" or new[i]== "-":
            if i > 0 and (new[i-1].isdigit() or new[i-1] == ")"):
                tokenlist.append(new[i])
                i += 1
            else:
                number = new[i]
                i += 1
                while i < len(new) and new[i].isdigit():
                    number += new[i]
                    i += 1
                tokenlist.append(number)
        elif new[i].isdigit():
            num = ""
            while i < len(new) and new[i].isdigit():
                num += new[i]
                i += 1
            tokenlist.append(num)
    return tokenlist

if __name__ == "__main__":
    inp = input('Enter your number:')
    print(tokenize(inp))