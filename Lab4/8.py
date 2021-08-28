ages = [81, 23, 10, 19, 91, 25, 55, 41, 49,
        60, 18, 32, 65, 10, 12, 13, 1, 2, 3]

# Just using lambda
adults = [lambda x=x: x for x in ages if x >= 18]
for adult in adults:
    print(adult())


adults = list(filter(lambda age: age > 18, ages))

print(adults)
