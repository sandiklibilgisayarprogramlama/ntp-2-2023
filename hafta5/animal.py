class Animal:
    def __init__(self, name, id, age) -> None:
        self.name = name
        self.id = id
        self.age = age

    def set_name(self, name):
        self.name = name

    def eat(self):
        print("animal eated")
