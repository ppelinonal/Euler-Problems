# Palindromik sayıyı kontrol eden fonksiyon
def palindromik(sayi):
    # Sayıyı stringe çevir ve tersini alarak kontrol et
    return str(sayi) == str(sayi)[::-1]

# İki 3 basamaklı sayının çarpımından oluşan en büyük palindromik sayıyı bulan fonksiyon
def en_buyuk_palindromik():
    en_buyuk = 0
    # 3 basamaklı sayılar arasında döngü
    for i in range(100, 1000):
        for j in range(i, 1000):
            carpim = i * j
            # Eğer çarpım palindromik ise ve mevcut en büyükten büyükse güncelle
            if palindromik(carpim) and carpim > en_buyuk:
                en_buyuk = carpim
    return en_buyuk

# Fonksiyonu çağır ve sonucu yazdır
print(en_buyuk_palindromik())
