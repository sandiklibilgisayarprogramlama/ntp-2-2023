from insan import Insan


class Ogretmen(Insan):
    def __init__(self, ad, soyad, yas, maas, meslek, brans):
        super().__init__(ad, soyad, yas, maas, meslek)
        self.brans = brans
