from insan import Insan

"""
miras alınan sinif super sınıf olarak adlandırılır.
"""


class Calisan(Insan):
    def __init__(self, ad, soyad, maas) -> None:
        super().__init__(ad, soyad)
        self.maas = maas

    def bilgi_yazdir(self):
        print(self.ad, " ", self.soyad)
