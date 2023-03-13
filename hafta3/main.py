from motor import Motor
from ucak import Ucak
from araba import Araba
from arac import Arac
#motor1 = Motor(120, 3, "benzin", True)

# motor1.bilgi_yazdir()

#ucak1 = Ucak(300, 5, "benzin", 150)
# ucak1.bilgi_yazdir()

araba1 = Araba(160, 4, "dizel", 4)
araba1.bilgi_yazdir()

print(dir(araba1))

print(araba1.__dict__)  # Sınıfın ad alanını içeren sözlük.
print(araba1.__doc__)  # Tanımlanmışsa, sınıf belgelendirme metni içerir.
print(Araba.__name__)  # sınıf adını getirir.
print(Araba.__base__)  # sınıfın miras aldığı (base) sınıfını getirir.
print(Arac.__base__)
print(araba1.__str__)
