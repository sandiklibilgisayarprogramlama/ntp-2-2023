from enstruman import Enstruman
from kisi import Kisi


class BasGitar(Enstruman):
    def __init__(self, ad: str, calan_kisi: Kisi, volume: int):
        super().__init__(ad, calan_kisi)
        self.volume = volume

    def cal(self):
        super().cal()
        print("Bas gitar çalıyor...")
