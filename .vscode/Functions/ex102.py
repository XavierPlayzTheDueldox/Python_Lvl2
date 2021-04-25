def recipe_shortcut(tsp, measurement):
    if measurement == 'tablespoons':
        tsp *= 3
    if measurement == 'cups':
        tsp *= 48
    c = tsp // 48
    tsp = tsp%48
    tbs = tsp // 3
    tsp = tsp%3

    return f'{c} cups, {tbs} tablespoons, {tsp} teaspoons'

tsp = int(input('Enter a number'))
measurement = input('Enter the measurement:')
print(recipe_shortcut(tsp, measurement))