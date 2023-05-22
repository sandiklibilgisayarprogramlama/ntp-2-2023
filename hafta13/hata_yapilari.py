"""
Hata Yakalama

try:
    Hata çıkabilecek kodlar
except:
    Hata çıkarsa çalışacak kodlar

Kod
------------------
print("Program başladı")

try:
    sayi1 = int(input("Birinci sayıyı giriniz: "))
    print(sayi1+10)
except:
    print("Hata oluştu")

print("naber")
print("Program bitti")
------------------------

# Hata türüne göre yakalama

try:
    Hata çıkabilecek kodlar
except HATA_TÜRÜ:
    Şu hata olursa çalışacak kodlar

try:
    sayi1 = int(input("Bir sayı giriniz: "))
    print(sayi1+10)
except TypeError:
    print("bir string ifadeyle sayı toplanamaz")
except ValueError:
    print("klavyeden sayı girmeniz gerekiyor")
except:
    print("bilinmeyen bir hata oluştu")

    
Hata çıksa bir şu kodu çalıştır (finally)
----------------------------------------------
try:
    sayi1 = int(input("Bir sayı giriniz: "))
    print(sayi1+10)
except:
    print("bir hata oluştu")
finally:
    print("Program sonlandı")
-------------------------------------------

except TypeError as hata1 -> hata1 değişkeni hata mesajını tutar

try:
    sayi1 = input("Bir sayı giriniz: ")
    print(sayi1+10)
except TypeError as hata1:
    print(hata1)
except ValueError:
    print("klavyeden sayı girmeniz gerekiyor")
except:
    print("bilinmeyen bir hata oluştu")
"""
