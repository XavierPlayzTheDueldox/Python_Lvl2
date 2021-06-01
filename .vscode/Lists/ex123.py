from ex122a import tokenize
from ex91 import precedence
def inf_2_pos(new):
    i = int()
    operatorlist = ['*', '/', '+', '-', "^"]
    operators = []
    postfix = []

    for i in range(len(new)):
        if new[i].lstrip('+-').isdigit():
            postfix.append(new[i])
        if new[i] in operatorlist:
            while (len(operators) != 0) and (operators[-1] != '(') and (precedence(new[i]) < precedence(operators[-1])):
                postfix.append(operators.pop())
            operators.append(new[i])
        if new[i] == '(':
            operators.append(new[i])
        if new[i] == ')':
            while operators[-1] != '(':
                postfix.append(operators.pop())
            operators.remove('(')

    while len(operators) != 0:
        postfix.append(operators.pop())

    return postfix

if __name__ == '__main__':
    inp = input('Enter the equation:')
    print(inf_2_pos(tokenize(inp)))

#Nvm about that common mistake lol
#it works tho for "3+4"
#vut is happening