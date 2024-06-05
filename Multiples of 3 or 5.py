# Toplam degerini 0'a esitliyoruz
sum = 0

# 0'dan 999a kadar numaralari geziyoruz dongude
for number in range(1000):
    # numara 3 veya 5in kati ise if komutunun icerisindeki koda giriyoruz
    if number % 3 == 0 or number % 5 == 0:
        # Kodun icerisinde isek o sayiyi toplama ekliyoruz
        sum += number

# Dongu bittikten sonra toplami gosteriyoruz
print(sum)
