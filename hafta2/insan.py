"""
super yada base class
"""


class Insan:

    goz_rengi = None

    def __init__(self, ad, soyad) -> None:
        self.ad = ad
        self.soyad = soyad

    def ad_yazdir(self):
        print(self.ad)
