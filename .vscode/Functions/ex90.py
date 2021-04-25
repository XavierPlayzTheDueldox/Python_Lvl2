def isInteger(string):
    return string.isdigit() or (string[0] == '+' or string[0] == '-') and string[1:len(string)].isdigit()
i = input("Enter the string:").strip()
print(isInteger(i))