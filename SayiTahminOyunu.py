## sayı tahmin oyunu - ders 28
import random
oyun_durumu = True

while oyun_durumu:
    hak = 7
    rastgele_sayi = random.randint(1, 100)
    print(""" ********* TAHMİN OYUNU *********** """)
    tahmin = int(input("Tahmininizi giriniz: "))
    while True:
        if tahmin == rastgele_sayi:
            print("KAZANDINIZ!")
            son = input("Tekrar oynamak ister misiniz(E/H): ")
            if son == "E":
                break
            elif son == "H":
                print("Çıkış yapılıyor...")
                oyun_durumu = False
                break
        if tahmin > rastgele_sayi:
            print("Sayı aşağıda!")
            hak -= 1
            tahmin = int(input("Kalan hak sayısı: {}\nTekrar deneyiniz: ".format(hak)))
        if tahmin < rastgele_sayi:
            print("Sayı yukarıda!")
            hak -= 1
            tahmin = int(input("Kalan hak sayısı: {}\nTekrar deneyiniz: ".format(hak)))
        if hak == 1:
            print("KAYBETTİNİZ!")
            son = input("Tekrar oynamak ister misiniz(E/H): ")
            if son == "E":
                break
            elif son == "H":
                print("Çıkış yapılıyor...")
                oyun_durumu = False
                break
