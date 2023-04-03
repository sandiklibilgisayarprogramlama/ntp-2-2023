from ogretmen import Ogretmen
from hademe import Hademe

ogretmen1 = Ogretmen("Ahmet", "uzun", 34, 20000, "Ogretmen", "Sınıf")
ogretmen2 = Ogretmen("Veli", "uzun", 38, 22000, "Ogretmen", "Matematik")

hademe1 = Hademe("Cemil", "Kısa", 35, 10000, "Hademe", 4)
hademe2 = Hademe("Ayşe", "Kısa", 28, 10000, "Hademe", 3)

if (hademe1.maas > hademe2.maas):
    print("Hademe1 daha fazla maas alıyor")
    print(hademe1.ad, hademe1.ad)
elif (hademe1.maas < hademe2.maas):
    print("Hademe2 daha fazla maas alıyor")
    print(hademe2.ad, hademe2.ad)
else:
    print("Hademeler aynı maasları alıyor")
