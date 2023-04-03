from maas import Maas


class Calisan:
    def __init__(self, isim, yas, ucret, bonus):
        self.isim = isim
        self.yas = yas
        self.maas = Maas(ucret, bonus)

    def toplam_maas(self):
        print(self.maas.yillik_ucret())
