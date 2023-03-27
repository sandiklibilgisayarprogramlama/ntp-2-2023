from animal import Animal


class Cat(Animal):
    def __init__(self, name, id, age, is_pet) -> None:
        super().__init__(name, id, age)
        self.is_pet = is_pet

    def eat(self):
        print(self.__class__.__name__)
        super().eat()
