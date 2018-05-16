import numpy


def primes(nb_primes: int):
    p = numpy.empty(nb_primes, dtype=int)

    n = 2
    len_p = 0

    while len_p < nb_primes:
        if not ((n % p[:len_p]) == 0).any():
            p[len_p] = n
            len_p += 1
        n += 1
    return p.tolist()


def primesfrom3to(n):
    """ Returns a array of primes, 3 <= p < n """
    sieve = numpy.ones(
        int(n / 2),
        dtype=numpy.bool)

    for i in range(3, int(n ** 0.5) + 1, 2):
        if sieve[int(i / 2)]:
            sieve[int(i * i / 2)::i] = False
    return 2 * numpy.nonzero(sieve)[0][1::] + 1


def ambi_sieve(n):
    # http://tommih.blogspot.com/2009/04/fast-prime-number-generator.html
    s = numpy.arange(3, n, 2)
    for m in range(3, int(n ** 0.5) + 1, 2):
        if s[int((m - 3) / 2)]:
            s[int((m * m - 3) / 2)::m] = 0
    return numpy.r_[2, s[s > 0]]
