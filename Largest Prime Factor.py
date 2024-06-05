def largest_prime_factor(n):
    # en kucuk bolenle basladik(initiate)
    factor = 2
    # en buyuk boleni depoladik(initiate)
    largest_factor = 1
    
    # Loop to find the prime factors
    while factor * factor <= n:
        # bolen sayinin n'i bolup bolmedigine bakiyoruz
        if n % factor == 0:
            # eger dogruysa en buyuk boleni guncelliyoruz
            n //= factor
            largest_factor = factor
        else:
            # eger degilse bir sonraki boleni deneyiyoruz
            factor += 1
    
    # n 1'den buyuk ise asal bolen ve en buyuk asal bolen
    if n > 1:
        largest_factor = n
    
    return largest_factor

# en buyuk asal bolenini bulmak istedigimiz sayi
number = 600851475143

# en buyuk asal boleni yazdiriyoruz
print(largest_prime_factor(number))
