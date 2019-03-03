"""

a script to calculate the number of rabbits after a certain number of generations based on a single pair of offspring
 roaslind FIBD
"""


class Rabbits(object):
    def __init__(self, n, k, m):
        """

        :param n: number of generations
        :param k: size of the litter - currently 1 needs fixing for more
        :param m: number of months the rabbit survives
        """
        self.generation = 0
        self.child = 1
        self.mature = 0
        self.adult = 0
        self.litter = k
        self.final_generation = n
        self.total = 0
        self.lifespan = m
        self.dead = 0
        self.offspring = [1]
        self.dead_list = []

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
        if self.generation < self.lifespan:
            print('too soon for deaths')
            pass
        else:
            self.dead = self.offspring[(self.generation - self.lifespan)]
            self.dead_list.append(self.dead)
            print(self.dead)
            print(f' dead list is {self.dead_list}')
            self.adult = self.adult - self.dead
        # print(f'total dead {self.dead}')
        return
        # print(f'total minus dead {self.adult}')

    def next_generation(self):
        self.total = self.adult + self.child
        # print(self.total)
        self.generation = self.generation + 1
        return

    def aging(self):
        self.child_aging()
        self.offspring_born()
        self.become_adults()
        # self.dead()
        self.next_generation()
        return

    def working_gen(self):
        while self.generation in range(0, self.final_generation):
            if self.generation == 0:
                self.next_generation()
            else:
                self.aging()
            print('generation: ' + str(f'{self.generation}') + ' total: ' + str(f'{self.total}')
                  + ' mature: ' + str(f'{self.mature}') + ' childs: ' + str(f'{self.child}'))
        return


Rabbits(7, 1, 4).working_gen()
