from arac import Arac


class Motor(Arac):
    def __init__(self, hiz, teker_sayisi, yakit_tipi, remork_varmi) -> None:
        super().__init__(hiz, teker_sayisi, yakit_tipi)
        self.remork_varmi = remork_varmi

    def bilgi_yazdir(self):
        print("Motor Bilgileri")
        super().bilgi_yazdir()
        print("Remork: ", self.remork_varmi)
