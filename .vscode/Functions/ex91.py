 def precedence(inp):
    if inp == '+' or inp == '-':
        return 1
    if inp == '*' or inp == '/':
        return 2
    if inp == '^':
        return 3
    else:
        return -1

inp == input("Enter a precedence:")
print(precedence(inp))