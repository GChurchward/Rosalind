"""

a script to calculate the probability of offspring with a dominact gene factor
    rosalind IPRB
"""

def prob(k, m, n):
    """

    :param k:  individuals are homozygous dominant for a factor
    :param m:  individuals are heterozygous dominant for a factor
    :param n:  individuals are homozygous recessive for a factor
    :return:    returns probability of offspring with dominant or recessive factor
    """

    total = k + m + n
    prob_kk = (k / total) * ((k - 1) / (total - 1))
    prob_km = (k / total) * (m / (total - 1))
    prob_kn = (k / total) * (n / (total - 1))
    prob_mm = (m / total) * ((m - 1) / (total - 1))
    prob_mn = (m / total) * (n / (total - 1))
    prob_nn = (n / total) * ((n - 1) / (total - 1))
    prob_mk = (m / total) * (k / (total - 1))
    prob_nk = (n / total) * (k / (total - 1))
    prob_nm = (n / total) * (m / (total - 1))
    print(prob_kk, prob_km, prob_kn, prob_mm, prob_mn, prob_nn, prob_mk, prob_nk, prob_nm)
    value = prob_kk + prob_km + prob_kn + prob_mm + prob_mn + prob_nn + prob_mk + prob_nk + prob_nm
    print(value)
    dominant = (prob_kk + prob_km + prob_kn + (prob_mm * 0.75) + (prob_mn * 0.5) + prob_mk + prob_nk + (prob_nm * 0.5))
    recessive = 1 - dominant
    print('Dominant = ' + str(dominant))
    print('Recessive = ' + str(recessive))
    return


prob(0, 2, 0)