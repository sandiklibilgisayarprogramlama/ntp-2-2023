from arac import Arac


class Ucak(Arac):
    def __init__(self, hiz, teker_sayisi, yakit_tipi, yolcu_sayisi) -> None:
        super().__init__(hiz, teker_sayisi, yakit_tipi)
        self.yolcu_sayisi = yolcu_sayisi

    def bilgi_yazdir(self):
        print("Ucak Bilgileri")
        super().bilgi_yazdir()
        print("Yolcu Bilgisi: ", self.yolcu_sayisi)

    # Nesne tabanlı programlamanın polimorfizm özelliği (Çok biçimlilik)
