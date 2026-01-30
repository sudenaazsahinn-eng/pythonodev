# Problem 1: Product Code Validator

ham_kod = input("Ürün kodunu giriniz: ")

#Kod temizleme işlemlerini yapacağız.
temiz_kod = ham_kod.replace(" ", "")
temiz_kod = temiz_kod.replace("/", "").replace("_", "").replace(".", "")
temiz_kod = temiz_kod.upper()
#Formata uygun hale getirelim.
if len(temiz_kod) == 10:
    temiz_kod = temiz_kod[0:4]+ "-" + temiz_kod[4:8] + "-" + temiz_kod[8:10]

print("Kodun temizlenmis hali:",temiz_kod)

#Temizlenen kodu doğrulayalım.
gecerli=True
hata= ""
# 1)Uzunluk kontrolü
#Not: Ürün kodu formatı(XXYY-NNNN-CC) toplamda 14 karakterdir fakat tireler silinince 12 karakter olacak.
if len(temiz_kod) !=12:
    gecerli = False
    hata= "Kod uzunluğu hatalı"
#2) Tirelerin kontrolü
elif temiz_kod[4] != "-" or temiz_kod[9] != "-":
    gecerli = False
    hata = "Tirelerin konumu yanlış"
else:
    #Format kurala uyuyor mu diye kontrol edelim.
    bolum1 = temiz_kod[0:2]    # XX
    bolum2 = temiz_kod[2:4]    # YY
    bolum3 = temiz_kod[5:9]    # NNNN
    bolum4 = temiz_kod[10:12]  # CC

    if not (bolum1.isalpha() and bolum2.isalpha() and bolum4.isalpha()):
        gecerli = False
        hata = "Harf kısmında hata var!"
    elif not bolum3.isdigit():
        gecerli = False
        hata = "Ürün numarası sayısal olmalı!"

# Sonuc
if gecerli:
    print("Durum:Geçerli ürün kodu = ", temiz_kod)
else:
    print("Durum:Geçersiz Ürün Kodu= ",hata)


#Problem 2: Smart Shopping Cart with Discounts

#Kullanıcıdan üyelik türünü ve ürün sayısını alalım.
uyelik_turu = input("Üyelik türünü giriniz (GOLD / SILVER / REGULAR / GUEST): ").upper()
urun_sayisi =int(input("Sepetteki ürün sayısını giriniz: "))

toplam_tutar = 0

#Toplam tutarı hesaplayalım.
for i in range(urun_sayisi):
    fiyat = float(input(f"{i+1}.ürünün fiyatını giriniz: "))
    toplam_tutar += fiyat

#Minimum tutarı geçiyor mu kontrol edelim.Sepet en az 50 TL olmalıdır
if toplam_tutar < 50:
    print("Hata: Sepet tutarı en az 50 TL olmalıdır!")
else:
    #Üyelik indirimleri
    if uyelik_turu == "GOLD": 
        uyelik_indirim_orani = 0.20
    elif uyelik_turu == "SILVER": 
        uyelik_indirim_orani = 0.10
    elif uyelik_turu == "REGULAR": 
        uyelik_indirim_orani = 0.05
    elif uyelik_turu == "GUEST":  
        uyelik_indirim_orani = 0
    else:
        uyelik_indirim_orani = 0
        print("Geçersiz üyelik türü, indirim uygulanmadı!")

    #İndirimi hesaplayalım ve indirimli tutarı bulalım.
    uyelik_indirimi = toplam_tutar * uyelik_indirim_orani
    indirimli_tutar = toplam_tutar - uyelik_indirimi

    #Toplu alım bonus indirimini hesaplayalım.
    bonus_indirimi = 0
    if indirimli_tutar > 500 and uyelik_turu != "GUEST":
        bonus_indirimi = indirimli_tutar * 0.05
        indirimli_tutar -= bonus_indirimi

    #Ödeme sonuçlarını ekrana yazdıralım.
    print("\n--- ÖDENECEK KISIM VE İNDİRİM ORANI --- ")
    print(f"Orijinal Toplam: {toplam_tutar:.2f} TL")
    print(f"Üyelik İndirimi: {uyelik_indirimi:.2f} TL")
    print(f"Toplu Alım Bonusu: {bonus_indirimi:.2f} TL")
    print(f"Ödenecek Tutar: {indirimli_tutar:.2f} TL")

#Problem 3: DNA Sequence Analyzer

# Kullanıcıdan DNA dizisini alıp, büyük harfe çevirip ,boşlukları silelim.
dna = input("DNA dizisini giriniz: ")
dna = dna.upper().replace(" ", "")

# 3) DNA dizisinin geçerli olup olmadığını kontrol et.(Sadece A, T, G, C harflerini içermeli)
if dna and all(harf in "ATGC" for harf in dna):
    #Dna uzunluğunu hesaplayalım.
    uzunluk = len(dna)

    #Nükleotid sayılarını hesaplayalım
    a = dna.count("A")
    t = dna.count("T")
    g = dna.count("G")
    c = dna.count("C")

    #GC oranını hesaplayalım.
    gc_orani = (g + c) / len(dna) * 100

    #Tamamlayıcı DNA dizisini oluşturalım.
    tamamlayici_dna = ""

    for harf in dna:
        if harf == "A":
            tamamlayici_dna += "T"
        elif harf == "T":
              tamamlayici_dna += "A"
        elif harf == "G":
              tamamlayici_dna += "C"
        elif harf == "C":
              tamamlayici_dna += "G"
    # Sonuçları ekrana yazdıralım
    print("\n--- DNA ANALİZ SONUÇLARI ---")
    print("DNA Dizisi:", dna)
    print("Toplam Uzunluk:", uzunluk)
    print("A Sayısı:", a)
    print("T Sayısı:", t)
    print("G Sayısı:", g)
    print("C Sayısı:", c)
    print("GC Oranı: % {:.2f}".format(gc_orani))
    print("Tamamlayıcı DNA Dizisi:", tamamlayici_dna)

else:
    # Geçersiz DNA dizisi durumu
    print("Hata: DNA dizisi sadece A, T, G ve C harflerini içermelidir!")


#Problem 4: Student Grade Manager

#Boş liste oluşturalım.
ogrenciler = []

#Öğrenci sayısını hatasız bir şekilde alalım.
while True:
    try:
        ogrenci_sayisi = int(input("Öğrenci sayısını giriniz(3-10): "))
        if 3 <= ogrenci_sayisi <= 10:
            break
        else:
            print("Hata: Öğrenci sayısı 3 ile 10 arasında olmalıdır!\n")
    except ValueError:
        print("Hata: Lütfen sadece sayı giriniz!\n")

#Öğrenci bilgilerini alalım.
for i in range(ogrenci_sayisi):
    isim = input(f"{i+1}. öğrencinin adını giriniz: ")

    #Notu hatasız bir şekilde alalım.
    while True:
        try:
            notu = int(input(f"{isim} adlı öğrencinin notunu giriniz (0-100): "))
            if 0 <= notu <= 100:
                break
            else:
                print("Hata: Not 0 ve 100 arasında olmalıdır! \n")
        except ValueError:
            print("Hata: Lütfen sadece sayı giriniz!\n")
    
    ogrenciler.append([isim, notu])

#Notları ayrı listeye alalım
notlar = [ogrenci[1] for ogrenci in ogrenciler]
en_yuksek = max(notlar)
en_dusuk = min(notlar)
ortalama = sum(notlar) / len(notlar)

#Sınıf istatistiklerini girelim.
print("\n--- SINIF İSTATİSTİKLERİ ---")
print("En yüksek not:", en_yuksek)
print("EN düşük not:", en_dusuk)
print("Sınıf ortalaması:", ortalama)

print("\n Ortalama üstü alan öğrenciler: ")
for ogrenci in ogrenciler:
    if ogrenci[1] > ortalama:
        print(f"- {ogrenci[0]} ({ogrenci[1]})")

#Problem 5
#Bonus Challenge:Palindrome Checker with Spaces and Punctuation Ignored

#Cümleyi alalım.
cumle = input("Bir cümle giriniz: ")

#Küçük harfe çevirelim,boşluk ve noktalama işaretlerini temizleyelim.
temiz_cumle = cumle.lower()

for karakter in [" ", ".", ",", "!", "?", ":", ";"]:
    temiz_cumle = temiz_cumle.replace(karakter, "")

#Tersini alalım, terminale yazdıralım ve karşılaştıralım.
ters_cumle = temiz_cumle[::-1]

print("\nGirilen cümle:", cumle)
print("Temizlenmiş cümle:", temiz_cumle)
print("Ters cümle:", ters_cumle)

if temiz_cumle == ters_cumle:
    print("Sonuç: Bu ifade PALİNDROMDUR.")
else:
    print("Sonuç: Bu ifade palindrom değildir!")

