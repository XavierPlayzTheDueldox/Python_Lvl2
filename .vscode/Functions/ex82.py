def taxi_fare(dist):
    return (((dist * 1000) // 140) * 0.25) + 4

distance = float(input('Enter the distance travelled:'))
print(f'The taxi fare is ${taxi_fare(distance):.2f}.')