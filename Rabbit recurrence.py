

class rabbits(object):
    def __init__(self, n, k):
        self.generation = 1
        self.child = 1
        self.mature = 0
        self.adult = 0
        self.litter = k
        self.final_generation = n
        self.total = 0

    def child_aging(self):
        self.mature = self.child
        return self.mature

    def offspring_born(self):
        self.child = self.adult * self.litter
        return self.child

    def become_adults(self):
        self.adult += self.mature
        return self.adult

    def next_generation(self):
        self.total = self.adult + self.child
        print(self.total)
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
            return print(self.final_generation, self.total)


