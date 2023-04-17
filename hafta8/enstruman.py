from kisi import Kisi


class Enstruman:
    __orkestrasi = "Boğaziçi"

    def __init__(self, ad: str, calan_kisi: Kisi):
        self.ad = ad
        self.calan_kisi = calan_kisi

    @property
    def orkestrasi(self):
        return self.__orkestrasi

    def cal(self):
        print(self.__orkestrasi, " çalıyor")
