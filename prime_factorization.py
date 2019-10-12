def prime_factorization(number):
    res = []
    prime_numbers = []
    x = 2
    prime_checker = []
    for i in range(2, int(number/4)):
        prime_checker.append(i)
    while x < int(number/2):
        checker = True
        for y in prime_checker:
            if x % y == 0:
                checker = False
                break
        if(checker):
            prime_numbers.append(x)
        x += 1
    print(prime_numbers)
    while not (number == 1):
        for x in prime_numbers:
            if number % x == 0:
                res.append(x)
                number = number/x
    return res
