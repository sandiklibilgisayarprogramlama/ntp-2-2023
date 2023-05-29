"""
Birden çok hata yakalama

try:
    sayi1=int(input("Birinci sayıyı giriniz: "))
    sayi2=int(input("İkinci sayıyı giriniz: "))
    print(sayi1/sayi2)
except (ZeroDivisionError,ValueError):
    print("Girilen değerler hatalıdır. ( 0 girilemez, sayı girilmelidir)")

print("Program sonlandı.")

--------------------------------------------------
Hata mesajını yazdırma

try:
    sayi1=int(input("Birinci sayıyı giriniz: "))
    sayi2=int(input("İkinci sayıyı giriniz: "))
    print(sayi1/sayi2)
except ZeroDivisionError as hata :
    print("Hata mesajı: ",hata)

print("Program sonlandı.")
-----------------------------------------------
Tüm hata mesajlarını yazdırma

try:
    sayi1=int(input("Birinci sayıyı giriniz: "))
    sayi2=int(input("İkinci sayıyı giriniz: "))
    print(sayi1/sayi2)
except Exception as hata :
    print("Hata mesajı: ",hata)

------------------------------------------------------
Belirlenen hata çıkması ama zerodivisionerror çıktı

try:
    bölünen = int(input("bölünecek sayı: "))
    bölen = int(input("bölen sayı: "))
except ValueError:
    print("Lütfen sadece sayı girin!")
else:
    try:
        print(bölünen/bölen)
    except ZeroDivisionError:
        print("Bir sayıyı 0'a bölemezsiniz!")

print("Program sonlandı.")
-------------------------------------------
try - except - finally

try:
    bölünen = int(input("bölünecek sayı: "))
    bölen = int(input("bölen sayı: "))
    print(bölünen/bölen)
except Exception as hata:
    print("Lütfen sadece sayı girin!")
finally:
    print("Program sonlandı.")

print("Program sonlandı.")
---------------------------------------------
raise


bölünen = int(input("bölünecek sayı: "))
bölen = int(input("bölen sayı: "))
if bölen<0:
    raise Exception("eksi sayı giremezsin")
print(bölünen/bölen)

print("Program sonlandı.")

assert vs. raise

giriş = input("Merhaba! Adın ne? ")
assert len(giriş) != 0 , "İsim bölümü boş."
print("Hoşgeldiniz.")
-----------------------------------------------------
giriş = input("Merhaba! Adın ne? ")
if len(giriş) == 0:
    raise AssertionError("İsim bölümü boş.")


"""
