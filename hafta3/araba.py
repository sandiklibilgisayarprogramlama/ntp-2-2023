from arac import Arac


class Araba(Arac):

    def __init__(self, hiz, teker_sayisi, yakit_tipi, kapi_sayisi) -> None:
        super().__init__(hiz, teker_sayisi, yakit_tipi)
        self.kapi_sayisi = kapi_sayisi

    def bilgi_yazdir(self):
        print("Araba Bilgileri")
        super().bilgi_yazdir()
        print("Kapı Sayısı", self.kapi_sayisi)
