"""

a script to determine the probability of n of a population having a certain trait
    rosalind LIA
"""
from math import factorial


def alleles(k, n, p=0.25):
    """

    :param k: number of generations
    :param n: number of organisms
    :param p: probability of success
    :return: numerator value of n c r
    """
    population = 2 ** k
    probabilities = []
    probability_n = 0
    if n > population:
        raise ValueError
    for n in range(n, population + 1):
        print(n)
        ncr = factorial(population) / (factorial(n) * factorial((population - n)))
        print(ncr)
        # number_success = p ** n
        # print(number_success)
        # number_fail = (1 - p) ** (population - n)
        # print(number_fail)
        combinations = ncr * (p ** n) * ((1 - p) ** (population - n))
        probabilities.append(combinations)
    print(probabilities)
    for idx in probabilities:
        probability_n += idx
    print(probability_n)
    return probability_n

alleles(5, 7)