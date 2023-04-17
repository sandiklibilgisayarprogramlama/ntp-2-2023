from enstruman import Enstruman
from kisi import Kisi


class Batari(Enstruman):
    def __init__(self, ad: str, calan_kisi: Kisi, davul_sayisi: int):
        super().__init__(ad, calan_kisi)
        self.davul_sayisi = davul_sayisi

    def cal(self):
        super().cal()
        print("batari caliyor...")
