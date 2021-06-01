def precedence(inp):
    if inp == '+' or inp == '-':
        return 1
    elif inp == '*' or inp == '/':
        return 2
    elif inp == '^':
        return 3
    else:
        return -1

if __name__ == "__main__":
    inp == input("Enter a precedence:")
    print(precedence(inp))