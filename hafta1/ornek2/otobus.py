class Otobus:
    __bilet_ucret = 100  # private

    def __init__(self, yolcu_liste, sefer) -> None:
        self.yolcu_liste = yolcu_liste  # public
        self.sefer = sefer  # public

    @property
    def bilet_ucret(self):
        return self.__bilet_ucret

    @bilet_ucret.setter
    def bilet_ucret(self, yeni_ucret):
        self.__bilet_ucret = yeni_ucret

    @bilet_ucret.deleter
    def bilet_ucret(self):
        del self.__bilet_ucret

    def yolcu_bilgi_yazdir(self):  # public
        for yolcu in self.yolcu_liste:
            print(yolcu.ad + " "+yolcu.soyad)
