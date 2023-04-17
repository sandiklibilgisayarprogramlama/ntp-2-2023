class Kisi:
    def __init__(self, ad: str, soyad: str, tel: int, adres: str):
        self.ad = ad
        self.soyad = soyad
        self.tel = tel
        self.adres = adres

    def bilgi_yaz(self):
        print(self.ad)
        print(self.soyad)
        print(self.tel)
        print(self.adres)
