from cat import Cat
from dog import Dog

cat1 = Cat("boncuk", 1, 1, True)
cat1.eat()


dog1 = Dog("çakır", 1, 1, True)
print(dog1.name)
dog1.set_name("Tekir")
print(dog1.name)

dog1.eat()
