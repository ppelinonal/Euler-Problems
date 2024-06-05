# Fibonacci dizisinin çift sayıların toplamını hesaplayan fonksiyon
def fibonacci_cift_toplami(limit):
    # İlk iki Fibonacci terimini tanımla
    a, b = 1, 2
    # Çift sayıların toplamını tutacak değişkeni tanımla
    cift_toplam = 0
    
    # Fibonacci dizisindeki terimler limitin altındayken devam et
    while a <= limit:
        # Eğer terim çiftse, toplamı ekle
        if a % 2 == 0:
            cift_toplam += a
        # Fibonacci dizisindeki bir sonraki terimi hesapla
        a, b = b, a + b
    
    return cift_toplam

# 4 milyon limitini tanımla
limit = 4000000
# Fonksiyonu çağır ve sonucu yazdır
print(fibonacci_cift_toplami(limit))
