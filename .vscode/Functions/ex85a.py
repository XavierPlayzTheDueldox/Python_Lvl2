number = ['first','second','third','fourth','fifth','sixth','seventh','eighth','ninth','tenth','eleventh','twelfth']
def ordinal(index):
    index -= 1
    if index > -1 and index < 13:
        return number[index]
    else: 
        return 'Sorry, your number is out of range'
    

if __name__ == "__main__":
    index = (int(input('Enter a number from one to twelve:'))) - 1
    print(ordinal(index))