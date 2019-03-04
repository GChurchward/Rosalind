"""

a script to determine the probability of n of a population having a certain trait
    rosalind LIA
"""


def alleles_numerator(k, n):
    """

    :param k: number of generations
    :param n: number of organisms
    :return: numerator value of n c r
    """
    population = 2 ** k
    if n > population:
        raise ValueError
    numerator = 1
    denominator = 1
    diff = population - n
    for value in range((population - diff), population):
        print(diff, population)
        numerator = numerator * value
        print(f' next value is {value}, total numerator = {numerator}')
    return numerator

def alleles_demoninator(k, n):
    """

    :param k: number of generations
    :param n: number of organisms
    :return: numerator value of n c r
    """
    for denom in range(1, n):
        denominator = denominator * denom
        print(f' next value is {value}, total denominator = {denominator}')
    print(denom)
    return denom

alleles_numerator(2, 1)