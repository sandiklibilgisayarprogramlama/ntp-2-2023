# from module_name import class_name
from insan import Insan

insan1 = Insan(175, 70)
insan1.yas = 20
insan1.boy_yazdir()
print(insan1.yas)

insan2 = Insan(180, 75)
print(insan2.yas)


insan3 = Insan(190, 90)
insan3.yas = 30
print(insan3.yas)

insan3.dogum_tarihi = "10.10.2000"
# print(insan1.__memleket) hata verir.

print(dir(insan1))
"""
dir metodu -> dahili, build-in
bir değişken araciligiyle kullanibilecek metodlari ve degişkenleri 
gösterir.
"""

# print(insan1.__memleket)
# insan1.__memleket = 10
print(insan1.memleket)
insan1.memleket = "İstanbul"
print(insan1.memleket)

# insan1.__gizli_metod() hata verir
insan1.gizli_is()
