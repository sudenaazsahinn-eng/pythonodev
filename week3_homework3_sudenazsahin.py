# Problem 1: Sensor Data Logger

def collect_readings (adet):

    #Kullanıcıdan belirtilen sayıda sıcaklık değeri alalım ve
    #Hatalı girişlerde tekrar isteyelim.
    okumalar = []
    i = 1

    while len(okumalar) < adet:
        try:
            deger = float(input(f"{i}. sıcaklık değerini giriniz: "))
            okumalar.append(deger)
            i += 1
        except ValueError:
            print("Hatalı giriş yaptınız lütfen sayısal bir değer giriniz!")

    return okumalar
def calculate_statistics (okumalar):
     #Sıcaklık değerlerinden istatistik hesaplamaları yapalım.
    istatistik = {
        "count" : len(okumalar),
        "average": round(sum(okumalar) / len(okumalar), 2),
        "minimum": round(min(okumalar), 2),
        "maximum": round(max(okumalar), 2),
        "range": round(max(okumalar) - min(okumalar) ,2)
    }
    return istatistik
def generate_report(istatistik):
    #İstatistikleri ekrana yazdıralım ve dosyaya kaydedelim.
    rapor = (
        "\n  SICAKLIK RAPORU  \n"
        f"Toplam Ölçüm Sayısı: {istatistik['count']}\n"
        f"Ortalama Sıcaklık: {istatistik['average']} °C\n"
        f"Minimum Sıcaklık: {istatistik['minimum']} °C\n"
        f"Maksimum Sıcaklık: {istatistik['maximum']} °C\n"
        f"Sıcaklık Aralığı: {istatistik['range']} °C\n"
    )
    print(rapor)

    with open("temperature_report.txt", "w", encoding="utf-8") as dosya:
        dosya.write(rapor)

    print("Rapor 'temperature_report.txt' dosyasına kaydedildi.")

#Programın ana kısmını yazdıralım.

while True:
    try:
        adet = int(input("Kaç tane sıcaklık ölçümü gireceksiniz? (3-10): "))
        if 3 <= adet <= 10:
            break
        else:
            print("Lütfen 3 ile 10 arasında bir sayı giriniz.")
    except ValueError:
        print("Lütfen geçerli bir sayı giriniz.")

okumalar = collect_readings(adet)
istatistik =calculate_statistics(okumalar)
generate_report(istatistik)

#-----------------------------------------------------------------------------

#Problem 2: Student Database Manager

#Boş bir öğrenci veritabanı oluşturacağız.
ogrenci_veritabani = {}

#Öğrenci ekleme fonksiyonunu yazalım.
def ogrenci_ekle(veritabani, ogrenci_no, ad, yas, notu, bolum):
    #Öğrenci numarası varsa uyarı verdirelim.
    if ogrenci_no in veritabani :
        print("Bu öğrenci numarası kayıtlı!")
    else:
        #Öğrenci bilgilerini sözlük olarak ekleyelim.
        veritabani[ogrenci_no] = {
            "ad" : ad,
            "yas" : yas,
            "not" : notu,
            "bolum" : bolum
        }

#Öğrenci numarasına göre arama fonksiyonunu yazalım.
def ogrenci_no_ile_ara(veritabani, ogrenci_no):
    if ogrenci_no in veritabani:
        return veritabani[ogrenci_no]
    else:
        return None
    
#Onur öğrencilerini bulan fonksiyon (not >= 85)
def onur_ogrencilerini_getir(veritabani, esik=85.0):
    onur_listesi = []
    for ogrenci_no, bilgiler in veritabani.items():
        if bilgiler["not"] >= esik :
            onur_listesi.append(ogrenci_no)

    return onur_listesi

#Bölüme göre not ortalması hesaplayan fonksiyonu yazalım.
def bolum_not_ortalamasi(veritabani, bolum_adi):
    toplam = 0
    sayac = 0
    for bilgiler in veritabani.values():
        if bilgiler["bolum"] == bolum_adi:
            toplam += bilgiler["not"]
            sayac += 1

    if sayac == 0:
        return 0.0
    else:
        return toplam / sayac


#Programın ana kısmını yazdıralım.
#Öğrencileri ekleyelim.
ogrenci_ekle(ogrenci_veritabani, "S101", "Alice", 20, 88.5, "Bilgisayar Mühendisliği")         
ogrenci_ekle(ogrenci_veritabani, "S102", "Bob", 21, 76.0, "Elektrik Mühendisliği")
ogrenci_ekle(ogrenci_veritabani, "S103", "Charlie", 19, 92.0, "Bilgisayar Mühendisliği")
ogrenci_ekle(ogrenci_veritabani, "S104", "Diana", 20, 81.5, "Makine Mühendisliği")
ogrenci_ekle(ogrenci_veritabani, "S105", "Eve", 22, 87.0, "Bilgisayar Mühendisliği")

#Tüm öğrencileri yazdıralım.
print("\n  ÖĞRENCİ VERİTABANI  ")
for ogrenci_no, bilgiler in ogrenci_veritabani.items():
    print(f"{ogrenci_no}: {bilgiler['ad'] } ({bilgiler['yas']}) - {bilgiler['bolum']} - Not: {bilgiler['not']}")
#Öğrencileri arayalım.
aranan_no = "S102"
sonuc = ogrenci_no_ile_ara(ogrenci_veritabani, aranan_no)

print(f"\nAranan Öğrenci Numarası: {aranan_no}")
if sonuc:
    print(f"Bulundu: {sonuc['ad']} ({sonuc['yas']}) - {sonuc['bolum']} - Not: {sonuc['not']}")   
else:
    print("Öğrenci bulunamadı.")

#Onur öğrencilerini yazdıralım.
onur_ogrencileri = onur_ogrencilerini_getir(ogrenci_veritabani)

print("\n--- ONUR ÖĞRENCİLERİ (Not ≥ 85) ---")
for ogrenci_no in onur_ogrencileri:
    print(f"{ogrenci_no}: {ogrenci_veritabani[ogrenci_no]['ad']} ({ogrenci_veritabani[ogrenci_no]['not']})")

#Bölüm not ortalamasını yazdıralım.    
bolum = "Bilgisayar Mühendisliği"
ortalama = bolum_not_ortalamasi(ogrenci_veritabani, bolum)

print(f"\nBölüm: {bolum}")
print(f"Not Ortalaması: {ortalama:.2f}") 

#-----------------------------------------------------------------------------

#Problem 3: Log File

def create_log_file(dosya_adi):
   #Belirtilen içerikle örnek bir log dosyası oluşturulur.
   log_icerigi = [
      "2024-12-10 09:00:15 | INFO | Server started successfully\n",
      "2024-12-10 09:05:22 | WARNING | High memory usage detected: 85%\n",
      "2024-12-10 09:10:45 | ERROR | Database connection failed\n",
      "2024-12-10 09:15:30 | INFO | User login: alice@example.com\n",
      "2024-12-10 09:20:18 | ERROR | File not found: config.json\n",
      "2024-12-10 09:25:55 | INFO | Backup completed successfully\n",
      "2024-12-10 09:30:12 | WARNING | Disk space running low: 15% remaining\n",
      "2024-12-10 09:35:40 | ERROR | API timeout: external service unavailable\n",
      "2024-12-10 09:40:25 | INFO | User logout: alice@example.com\n"
   ] 
   with open(dosya_adi, "w", encoding = "utf-8") as dosya:
      for satir in log_icerigi:
         dosya.write(satir)

#Log dosyasını analiz eden fonksiyonu yazalım.
def log_analiz_et(dosya_adi):
   toplam_satir = 0
   info_sayisi = 0
   warning_sayisi = 0
   error_sayisi = 0
   error_mesajlari =[]

   with open(dosya_adi, "r", encoding = "utf-8") as dosya:
      for satir in dosya:
         toplam_satir += 1

         if "INFO" in satir:
            info_sayisi += 1
         elif "WARNING" in satir:
            warning_sayisi += 1
         elif "ERROR" in satir:
            error_sayisi += 1
            #Sadece hata mesajını alalım.
            mesaj = satir.split("|")[-1].strip()
            error_mesajlari.append(mesaj)

   return{
      "toplam_satir": toplam_satir,
      "info": info_sayisi,
      "warning": warning_sayisi,
      "error": error_sayisi,
      "error_mesajlari": error_mesajlari
   }      

#Sadece ERROR satırlarını başka dosyaya yazdıran fonksiyonu kullanalım.
def sadece_error_kaydet(giris_dosyasi, cikis_dosyasi):
   hata_sayisi = 0
   with open(giris_dosyasi, "r", encoding = "utf-8") as giris, \
        open(cikis_dosyasi, "w", encoding="utf-8") as cikis:            
      
      for satir in giris:
         if "ERROR" in satir:
            cikis.write(satir)
            hata_sayisi += 1

   return hata_sayisi

#Programın ana kısmını yazdıralım.
log_dosyasi = "server_log.txt"
error_dosyasi = "errors_only.txt"

#Log dosyasını oluşturalım.
create_log_file(log_dosyasi)
print(f"Log dosyası oluşturuldu: {log_dosyasi}")

#Log dosyasını analiz edelim.
sonuc = log_analiz_et(log_dosyasi)
print("\n  LOG ANALİZİ  ")
print(f"Toplam Kayıt: {sonuc['toplam_satir']}")
print(f"INFO: {sonuc['info']}")
print(f"WARNING: {sonuc['warning']}")
print(f"ERROR: {sonuc['error']}")

print("\n Hata Mesajları: ")
for i, mesaj in enumerate(sonuc["error_mesajlari"], start = 1):
   print(f"{i}. {mesaj}")

#ERROR kayıtlarını ayrı dosyaya kaydeelim.
adet = sadece_error_kaydet(log_dosyasi, error_dosyasi)
print(f"\n Hatalar kaydedildi: {error_dosyasi}({adet} hata)")

#-----------------------------------------------------------------------------

#Problem 4: Inventory Management with CSV

#Envanteri başlatan fonksiyonu yazdıralım.
def envanteri_baslat():
    urunler = [
        ["P001", "Laptop", 15, 5000.00],
        ["P002", "Mouse", 5, 150.00],
        ["P003", "Klavye", 8, 300.00],
        ["P004", "Monitör", 20, 2000.00],
        ["P005", "USB Kablo", 3, 25.00]
    ]
    return urunler
#Ürünleri CSV dosyasıa kaydeden fonksiyonu yazalım.
def csv_kaydet(urunler, dosya_adi):
    with open(dosya_adi, "w", encoding="utf-8") as dosya:
        dosya.write("Urun_ID,Ad,Adet,Fiyat\n")
        #Ürünleri satır satır yazalım.
        for urun in urunler:
            dosya.write(f"{urun[0]},{urun[1]},{urun[2]},{urun[3]}\n")

#CSV dosyasından ürünleri okutalım.
def csv_yukle(dosya_adi):
    urunler = []
    try:
        with open(dosya_adi, "r", encoding="utf-8") as dosya:
            satirlar = dosya.readlines()[1:] 
            for satir in satirlar:
                urun_id, ad, adet, fiyat = satir.strip().split(",")
                urunler.append([urun_id, ad, int(adet), float(fiyat)])
    except FileNotFoundError:
        print("CSV dosyası bulunamadı!")
    return urunler

#Düşük stoklu ürünleri bulan fonksiyonu yazdıralım.
def dusuk_stok_bul(urunler, esik=10):
    dusuk_stoklar = []
    for urun in urunler:
        if urun[2] < esik:
            dusuk_stoklar.append({
                "urun_id": urun[0],
                "ad" : urun[1],
                "adet" : urun[2],
                "fiyat" : urun[3]
            })
    return dusuk_stoklar

#Programın ana kısmını yazdıralım.
dosya_adi = "inventory.csv"

#Envanteri oluşturalım,CSV dosyasını kaydedelim,CSV dosyasından tekrar yükleyelim.
urun_listesi = envanteri_baslat()
csv_kaydet(urun_listesi, dosya_adi)
print(f"Envanter kaydedildi : {dosya_adi}")
yuklenen_urunler = csv_yukle(dosya_adi)

#Tüm ürünleri yazdıralım.
print("\n   GÜNCEL ENVANTER   ")
for urun in yuklenen_urunler:
    print(f"{urun[0]}: {urun[1]} (Adet: {urun[2]}, Fiyat: {urun[3]:.2f} TL)")

#Düşük stoklu ürünleri bulalım
dusuk_stoklar = dusuk_stok_bul(yuklenen_urunler)

print("\n   DÜŞÜK STOK UYARISI (< 10)  ")
for urun in dusuk_stoklar:
    print(f"{urun['urun_id']}: {urun['ad']} (Adet: {urun['adet']})")

#-----------------------------------------------------------------------------

# BONUS: Word Frequency Counter from File

#Kullanıcıdan paragraf alalım.
metin = input("Bir paragraf giriniz: ")
#Metni dosyaya kaydedelim.
with open ("input_text.txt", "w", encoding="utf-8") as dosya:
    dosya.write(metin)
#Dosyayı okutup küçük harfe çevirelim.
with open("input_text.txt", "r", encoding="utf-8") as dosya:
    icerik = dosya.read().lower()

#Noktalama işaretlerini temizleyelim.
for karakter in ".,!?;:":
    icerik = icerik.replace(karakter, "")

#Kelime frekanslarını sözlükte tutalım.
kelimeler = icerik.split()
frekanslar = {}

for kelime in kelimeler:
    if kelime in frekanslar:
        frekanslar[kelime] += 1
    else:
        frekanslar[kelime] = 1

#En çok tekrar eden 5 kelimeyi gösterelim.
sirali = sorted(frekanslar.items(), key=lambda x: x[1], reverse=True)
print("\n   EN ÇOK GEÇEN 5 KELİME   ")
for kelime, adet in sirali[:5]:
    print(f"{kelime}: {adet}")

#Tüm sonuçları kaydedelim.
with open("word_frequency.txt", "w", encoding="utf-8") as dosya:
    for kelime, adet in sirali:
        dosya.write(f"{kelime}: {adet}\n")

print("\n Kelime frekans raporu 'word_frequency.txt' dosyasına kaydedildi.")
