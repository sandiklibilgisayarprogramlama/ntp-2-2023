class Person:
    def __init__(self, name: str, address: str):
        self.name = name
        self.address = address

    def get_name(self) -> str:
        return self.name

    def get_address(self) -> str:
        return self.address
