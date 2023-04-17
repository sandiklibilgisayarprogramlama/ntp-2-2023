from kisi import Kisi
from gitar import Gitar
from bas_gitar import BasGitar
from batari import Batari

kisi1 = Kisi("ahmet", "uzun", 5069332244, "merkez/sandikli")
kisi1.bilgi_yaz()

gitar1 = Gitar("Şeref", kisi1, 8)
gitar1.cal()

bas_gitar1 = BasGitar("ahmet", kisi1, 20)
bas_gitar1.cal()

batari1 = Batari("ismail", kisi1, 5)
batari1.cal()

print(batari1.calan_kisi.ad)
print(batari1.orkestrasi)
batari1.orkestrasi = "dasda"
