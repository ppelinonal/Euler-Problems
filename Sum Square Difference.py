# İlk n doğal sayının kareleri toplamını hesaplayan fonksiyon
def kareler_toplami(n):
    toplam = 0
    for i in range(1, n + 1):
        toplam += i ** 2
    return toplam

# İlk n doğal sayının toplamını hesaplayan fonksiyon
def toplam(n):
    toplam = 0
    for i in range(1, n + 1):
        toplam += i
    return toplam

# İlk 100 doğal sayının kareleri toplamı
n = 100
kareler_toplami_100 = kareler_toplami(n)

# İlk 100 doğal sayının toplamı ve bu toplamın karesi
toplam_100 = toplam(n)
toplam_karesi_100 = toplam_100 ** 2

# İki değer arasındaki fark
fark = toplam_karesi_100 - kareler_toplami_100

# Sonucu yazdır
print(fark)
