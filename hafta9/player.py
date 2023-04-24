from person import Person
from position import POSITION


class Player(Person):
    def __init__(self, name: str, address: str, number: int, position: POSITION):
        super().__init__(name, address)
        self.number = number
        self.position = position

    def get_position(self) -> POSITION:
        return self.position
