def primes(nb_primes: int):

    p = []

    if nb_primes > 1000:
        nb_primes = 1000

    len_p = 0  # The current number of elements in p.
    n = 2
    while len_p < nb_primes:
        # Is n prime?
        for i in p:
            if n % i == 0:
                break

        # If no break occurred in the loop, we have a prime.
        else:
            p.append(n)
            len_p += 1
        n += 1

    # Let's return the result in a python list:
    return p
