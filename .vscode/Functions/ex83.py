def shipping_charge(number):
    return ((number-1) * 2.95) + 10.95

items = float(input('Enter the number of items purchased:'))
print(f'The shipping charge for all your items is ${shipping_charge(items):.2f}.')