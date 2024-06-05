def nth_prime(number):
    largest_prime = 2
    
    #2'den girilen sayiya kadar olan numaralari donguye aliyoruz
    for i in range(2, number):
        is_prime = True
        
        # 'i' asal sayi mi diye bakiyoruz
        for n in range(2, i):
            if i % n == 0:
                is_prime = False
                break  #'i'nin asal olmadigini ogrenip donguden cikiyoruz
        
        #'i' prime ise en buyuk prime(largest_prime) degerine esitliyoruz
        if is_prime:
            largest_prime = i
    
    return largest_prime

# Main kodumuz
number = int(input("Lutfen kendisinden kucuk en buyuk asal sayiyi bulmak istediginiz sayiyi giriniz: "))
print(nth_prime(number))
