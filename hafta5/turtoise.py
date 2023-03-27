from animal import Animal


class Turtoise(Animal):
    def __init__(self, name, id, age, shell_status) -> None:
        super().__init__(name, id, age)
        self.shell_status = shell_status

    def eat(self):
        print(self.__class__.__name__)
        super().eat()
