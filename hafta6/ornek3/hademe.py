from insan import Insan


class Hademe(Insan):
    def __init__(self, ad, soyad, yas, maas, meslek, gorevli_kat):
        super().__init__(ad, soyad, yas, maas, meslek)
        self.gorevli_kat = gorevli_kat
