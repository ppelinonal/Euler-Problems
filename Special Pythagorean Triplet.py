# Pisagor üçlüsünü bulan ve abc ürününü hesaplayan fonksiyon
def pisagor_uclusu_toplam(limit):
    for a in range(1, limit):
        for b in range(a + 1, limit - a):
            c = limit - a - b
            if a**2 + b**2 == c**2:
                return a * b * c

# 1000 limitini tanımla
limit = 1000
# Fonksiyonu çağır ve sonucu yazdır
print(pisagor_uclusu_toplam(limit))
