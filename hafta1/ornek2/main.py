from otobus import Otobus
from yolcu import Yolcu


yolcu1 = Yolcu("Yusuf", "yıldız", 10)
yolcu2 = Yolcu("İbrahim", "yıldız", 15)
yolcu3 = Yolcu("Mert", "yıldız", 20)

otobus1 = Otobus([yolcu1, yolcu2, yolcu3], "Afyon - Ankara")
print(otobus1.bilet_ucret)
# print(otobus1.__bilet_ucret)
otobus1.bilet_ucret = 200
print(otobus1.bilet_ucret)

otobus1.yolcu_bilgi_yazdir()
