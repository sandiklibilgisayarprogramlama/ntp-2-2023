class Insan:
    yas = None  # public, aleni
    dogum_tarihi = None  # public
    __memleket = "Afyon"  # private, gizli

    # nesne uretildiginde calisan ilk metod

    def __init__(self, boy, kilo):
        self.boy = boy
        self.kilo = kilo

    def boy_yazdir(self):
        print(self.boy)

    @property  # okuma yapma imkanı sağlar
    def memleket(self):
        return self.__memleket

    @memleket.setter  # atama yapma imkanı sağlar
    def memleket(self, yeni_memleket):
        self.__memleket = yeni_memleket

    def __gizli_metod(self):
        print("çok gizli")

    def gizli_is(self):
        self.__gizli_metod()
