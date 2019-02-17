
#def mortal_rabbits(offspring, generations, lifespan):
#    sequence = [1, 1]
#    month_offspring = [0, 0]
#    for i in range(2, lifespan):
#        sequence[i] = sequence[n]
#    print(a, b)
#    for d in range(lifespan, generations):
#        a, b = b, (offspring * a + b - c)
#    print(b)
#    return
#
#mortal_rabbits(1, 6, 3)



class rabbits(object):
    def __init__(self, n, k, m):
        self.generation = 1
        self.child = 1
        self.mature = 0
        self.adult = 0
        self.litter = k
        self.final_generation = n + 1
        self.total = 0
        self.lifespan = m
        self.dead = 0
        self.offspring = []

    def child_aging(self):
        self.mature = self.child
        return self.mature

    def offspring_born(self):
        self.child = self.adult * self.litter
        self.offspring.append(self.child)
        print(self.offspring)
        return self.child

    def become_adults(self):
        self.adult += self.mature
        print(f'adults {self.adult}')
        if (self.generation - 1) < (self.lifespan):
            pass
        else:
            self.dead = self.offspring[(self.generation - self.lifespan)]
            print(self.dead)
            self.adult = self.adult - self.dead
        print(f'total dead {self.dead}')
        print(f'total minus dead {self.adult}')
        return self.adult

    def next_generation(self):
        self.total = self.adult + self.child
        #print(self.total)
        self.generation = self.generation + 1
        return

    def aging(self):
        self.child_aging()
        self.offspring_born()
        self.become_adults()
        self.next_generation()
        return

    def working_gen(self):
        while self.generation in range(1, self.final_generation):
            if self.generation == 1:
                self.next_generation()
            else:
                self.aging()
            print('generation: ' + str(f'{self.generation}') + ' total: ' + str(f'{self.total}'))
        return

rabbits(6, 1, 3).working_gen()
