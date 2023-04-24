from person import Person
from accr_level import ACCRLEVEL


class Coach(Person):
    def __init__(self, name: str, address: str, accreditation_level: ACCRLEVEL, experience: int):
        super().__init__(name, address)
        self.accreditation_level = accreditation_level
        self.experience = experience
