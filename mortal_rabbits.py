
def mortal_rabbits(offspring, generations, lifespan):
    sequence = [1, 1]
    a = sequence[i]
    b = sequence[(i + 1)]
    c = sequence[(i - lifespan)]
    for i in range(2, lifespan):
        sequence[i] = sequence[n]
    print(a, b)
    for d in range(lifespan, generations):
        a, b = b, (offspring * a + b - c)
    print(b)
    return

mortal_rabbits(1, 6, 3)