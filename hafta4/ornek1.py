class Insan:
    def __init__(self, ad, soyad, yas, cinsiyet) -> None:
        self.ad = ad
        self.soyad = soyad
        self.yas = yas
        self.cinsiyet = cinsiyet

    def adini_ekrana_yaz(self):
        print(self.ad)
