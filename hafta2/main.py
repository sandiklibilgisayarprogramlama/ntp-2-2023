from calisan import Calisan
from ogrenci import Ogrenci
from musteri import Musteri

calisan1 = Calisan("ahmet", "taş", 10000)
calisan1.bilgi_yazdir()

musteri1 = Musteri("İsmail", "Uzun", "merkez/sandıklı")

ogrenci1 = Ogrenci("Serkan", "Uzun", 2000)
print(ogrenci1.ad)
print(ogrenci1.goz_rengi)

print(musteri1.goz_rengi)

ogrenci1.ad_yazdir()
musteri1.ad_yazdir()
calisan1.ad_yazdir()
