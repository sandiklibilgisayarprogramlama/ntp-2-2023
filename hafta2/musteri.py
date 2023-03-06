from insan import Insan

"""
miras alan alt sınıf (subclass) adı verilir.
"""


class Musteri(Insan):
    def __init__(self, ad, soyad, adres) -> None:
        super().__init__(ad, soyad)
        self.adres = adres
