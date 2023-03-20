class Sofor:
    def __init__(self, ad, soyad) -> None:
        self.ad = ad
        self.soyad = soyad


class Araba:
    def __init__(self, marka, model, surucu, sunroof) -> None:
        self.marka = marka
        self.model = model
        self.surucu = surucu
        self.__sunroof = sunroof

    @property
    def sunroof(self):
        return self.__sunroof

    @sunroof.setter
    def sunroof(self, val):
        self.__sunroof = val


sofor1 = Sofor("ismail", "uzun")
araba1 = Araba("opel", "1990", sofor1, False)
print(araba1.sunroof)

araba1.sunroof = True
print(araba1.sunroof)
