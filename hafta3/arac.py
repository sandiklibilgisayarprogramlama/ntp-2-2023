class Arac:
    def __init__(self, hiz, teker_sayisi, yakit_tipi) -> None:
        self.hiz = hiz
        self.teker_sayisi = teker_sayisi
        self.yakit_tipi = yakit_tipi

    def bilgi_yazdir(self):
        print("Hız: ", self.hiz)
        print("Yakıt Tipi: ", self.yakit_tipi)
        print("Teker Sayısı: ", self.teker_sayisi)


"""
Pyhonda her sınıf bir base sınıftan türetilir.
class Oyuncu(object): = class Oyuncu:
pythonda her sınıf objectten türemiştir.
"""
