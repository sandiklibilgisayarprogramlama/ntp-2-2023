from enstruman import Enstruman
from kisi import Kisi


class Gitar(Enstruman):
    def __init__(self, ad: str, calan_kisi: Kisi,  tel_sayisi: int):
        super().__init__(ad, calan_kisi)
        self.tel_sayisi = tel_sayisi

    def cal(self):
        super().cal()
        print("gitar çaldı")
