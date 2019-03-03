"""

a script to calculate the expected number of offspring with a dominant phenotype
    rosalind IEV
"""

def expected_offspring(kk, km, kn, mm, mn, nn, offspring=2):
    """

    :param kk: AA-AA couple are both homozygous dominant for a factor
    :param km: AA-Aa couple are homozygous and heterozygous dominant for a factor
    :param kn: AA-aa couple are homozygous dominant and homozygous recessive for a factor
    :param mm: Aa-Aa couple are both heterozygous dominant for a factor
    :param mn: Aa-aa couple are heterozygous dominant and homozygous recessive for a factor
    :param nn: aa-aa couple are both homozygous recessive
    :param offspring number of offspring each couple is expected to have
    :return: expected number of offspring displaying dominant phenotype
    """

    offspring_k = kk + (0.5 * km) + (0.25 * mm)
    offspring_m = (0.5 * km) + kn + (0.5 * mm) + (0.5 * mn)
    offspring_n = (0.25 * mm) + (0.5 * mn) + nn
    total = offspring_m + offspring_n + offspring_k
    expected_dominant = (offspring_k + offspring_m) * offspring
    expected_recessive = offspring_n * offspring
    percent_total_dom = expected_dominant / (total * offspring)
    percent_total_rec = expected_recessive / (total * offspring)
    print(expected_dominant)
    print(expected_recessive)
    print(offspring_k, offspring_m, offspring_n)
    print('% of population dominant: ' + str(percent_total_dom))
    print('% of population recessive: ' + str(percent_total_rec))
    return

expected_offspring(1, 0, 0, 1, 0, 1)

expected_offspring(18474, 18889, 18780, 19321, 19782, 16428)