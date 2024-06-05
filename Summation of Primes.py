# Asal sayı kontrolü yapan fonksiyon
def asal_mi(sayi):
    if sayi <= 1:
        return False
    if sayi == 2:
        return True
    if sayi % 2 == 0:
        return False
    for i in range(3, int(sayi**0.5) + 1, 2):
        if sayi % i == 0:
            return False
    return True

# İki milyonun altındaki asal sayıların toplamını hesaplayan fonksiyon
def iki_milyon_altindaki_asallar_toplami(limit):
    toplam = 0
    for sayi in range(2, limit):
        if asal_mi(sayi):
            toplam += sayi
    return toplam

# 2 milyon limitini tanımla
limit = 2000000
# Fonksiyonu çağır ve sonucu yazdır
print(iki_milyon_altindaki_asallar_toplami(limit))
