# PROBLEM 1: Smart Temperature Converter
try:
#Kullanıcıdan bir sıcaklık değeri(float) ve birim girişi isteyiniz.
    sicaklik = float(input("Sıcaklık değerini giriniz: "))
    birim = input("Birimi giriniz (C veya F): ").upper()
    if birim == "C":
        #Celsius'u Fahrenheit'a dönüştürmek için: F = (C *9/5) + 32
        sonuc = (sicaklik * 9/5) + 32
        print(f"{sicaklik:.2f}°C eşittir {sonuc:.2f}°F") # 2 ondalık basamak 
    elif birim == "F":
        # Fahrenheit'ı Celsius'a dönüştürmek için: C = (F - 32) * 5/9 
        sonuc = (sicaklik - 32) * 5/9
        print(f"{sicaklik:.2f}°F eşittir {sonuc:.2f}°C") # 2 ondalık basamak 
    else:
        print("Hata: Lütfen sadece 'C' veya 'F' giriniz.")

except ValueError:
    #Geçersiz sayı girişini kontrol etme.
    print("Hata: Lütfen geçerli bir sayı giriniz!")


# PROBLEM 2: Binary Clock Display
try:
    #Kullanıcıdan saat ve dakika girişi alınız.
    saat = int(input("Saati giriniz (0-23): "))
    dakika = int(input("Dakikayı giriniz (0-59): "))

    if 0<= saat <=23 and 0<= dakika <=59:
        #Zamanı standart formatta gösterme (HH:MM)
        print(f"Zaman: {saat:02d}:{dakika:02d}")
        #Saat ve Dakikayı ikili(binary) formatta gösteriniz.(Başında '0b' olmadan gösterin)
        print(f"Saatin ikilik karşılığı: {bin(saat)[2:]}") 
        print(f"Dakikanın ikilik karşılığı: {bin(dakika)[2:]}")
    else:
        print("Hata: Saat 0-23, dakika 0-59 aralığında olmalıdır.")

except ValueError:
    print("Hata: Lütfen sayısal değer giriniz!")


# PROBLEM 3: Salary Calculator with Tax Brackets
try:
    #Kullanıcıdan yıllık brüt maaşını isteyiniz.
    brut_maas = float(input("Yıllık brüt maaşınızı giriniz: "))
    
    #Uygulanacak vergi miktarlarını belirtelim.
    if brut_maas <= 50000:
        vergi_orani = 0.10
    elif brut_maas <= 100000:
        vergi_orani = 0.15
    else:
        vergi_orani = 0.20

    vergi_miktari = brut_maas * vergi_orani
    net_maas = brut_maas - vergi_miktari

    #Maaşları binlik ayraç kullanarak, vergi miktarını ise 2 ondalık basamakla gösterim.
    print(f"Brüt Maaş: {brut_maas:,.2f} TL")
    print(f"Vergi Miktarı: {vergi_miktari:,.2f} TL (%{int(vergi_orani * 100)})")
    print(f"Net Maaş: {net_maas:,.2f} TL")
except ValueError:
    print("Hata: Maaş için sayısal bir değer girmelisiniz!")


# PROBLEM 4: Password Strength Checker

#Kullanıcıdan bir şifre oluşturmasını isteyiniz.
sifre = input("Bir şifre oluşturunuz: ")

#Şartları kontrol edelim.En az 8 karakter uzunluğunda olmalı.
#En az bir rakam (0-9) içermeli.En az bir büyük harf içermeli.
uzunluk_kontrol = len(sifre) >= 8
rakam_kontrol = any(karakter.isdigit() for karakter in sifre)
buyuk_harf_kontrol = any(karakter.isupper() for karakter in sifre)

#Şartların sağlanıp sağlanmadığını yazdıralım.
print(f"En az 8 karakter: {'Sağlandı' if uzunluk_kontrol else 'Sağlanmadı'}")
print(f"Rakam içeriyor mu: {'Sağlandı' if rakam_kontrol else 'Sağlanmadı'}")
print(f"Büyük harf içeriyor mu: {'Sağlandı' if buyuk_harf_kontrol else 'Sağlanmadı'}")
#Şifre kabul edildi mi kontrolü
if uzunluk_kontrol and rakam_kontrol and buyuk_harf_kontrol:
    print("Şifre Kabul Edildi (Password Accepted)!")
else:
    print("Şifre Reddedildi (Password Rejected)!")


# Problem 5: RGB → HEX Renk Dönüştürücü
try:
    #Kullanıcıdan renk değerlerini alınız.
    kirmizi = int(input("Kırmızı değerini giriniz (0-255): "))
    yesil = int(input("Yeşil değerini giriniz (0-255): "))
    mavi = int(input("Mavi değerini giriniz (0-255):"))

    #0-255 aralığında mı kontrolü
    if 0 <= kirmizi <=255 and 0 <= yesil <= 255 and 0 <= mavi <=255:
        ##Hexadecimal'e dönüştürme ve eğer tek karakterliyse 2 haneye tamamlama 
        hex_kodu = f"#{kirmizi:02X}{yesil:02X}{mavi:02X}"
        print(f"RGB({kirmizi}, {yesil}, {mavi}) = {hex_kodu}")

    else:
        print("Hata:RGB değerleri 0-255 arasında olmalıdır.")

except ValueError:
    print("Hata:Sadece sayısal değer giriniz!")

