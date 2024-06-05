import math

# İki sayının en küçük ortak katını (EKOK) hesaplayan fonksiyon
def ekok(a, b):
    return abs(a*b) // math.gcd(a, b)

# 1'den 20'ye kadar olan sayıların EKOK'unu hesaplayan fonksiyon
def en_kucuk_pozitif_sayi(limit):
    sonuc = 1
    for i in range(1, limit + 1):
        sonuc = ekok(sonuc, i)
    return sonuc

# 20 limitini tanımla
limit = 20
# Fonksiyonu çağır ve sonucu yazdır
print(en_kucuk_pozitif_sayi(limit))
