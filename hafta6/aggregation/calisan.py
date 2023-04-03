class Calisan:
    def __init__(self, isim, yas, maas) -> None:
        self.isim = isim
        self.yas = yas
        self.maas = maas

    def toplam_ucret(self):
        print(self.maas.yillik_maas())
