from insan import Insan


class Ogrenci(Insan):
    def __init__(self, ad, soyad, hizmet_ucret) -> None:
        super().__init__(ad, soyad)
        self.hizmet_ucret = hizmet_ucret
