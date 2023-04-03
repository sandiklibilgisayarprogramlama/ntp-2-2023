class Maas:
    def __init__(self, ucret, bonus):
        self.ucret = ucret
        self.bonus = bonus

    def yillik_maas(self):
        return (self.ucret*12)+self.bonus
