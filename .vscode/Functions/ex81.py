
def hypothenuse(side1, side2):
    return (side1*side1 + side2*side2) ** 0.5

ans1 = int(input('Enter the shorter side of a triangle:'))
ans2 = int(input('Enter the other shorter side of a triangle:'))
print(f'The length of the hypothenuse is {hypothenuse(ans1,ans2)}.')