from ex122a import tokenize
from ex123 import inf_2_pos
def eva_postfix(new):
    values = list()
    for token in new:
        if token.lstrip('+-').isdigit():
            values.append(int(token))
        else:
            right = values.pop()
            left = values.pop()
            if token == '+':
                add = left + right
            elif token == '-':
                add = left - right
            elif token == '/':
                add = left / right
            elif token == '^':
                add = left ** right
            else:
                add = left * right
            values.append(add)
    return values[0]

inp = input('Enter your equation:')
print(eva_postfix(inf_2_pos(tokenize(inp))))
