def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")

    i = 1
    factors = []
    while i < number:
        if number % i == 0:
            factors.append(i)
        i += 1
        continue

    aliquot_sum = sum(factors)

    if aliquot_sum > number:
        return 'abundant'
    if aliquot_sum < number:
        return 'deficient'
    if aliquot_sum == number:
        return 'perfect'
