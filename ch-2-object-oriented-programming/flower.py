# R-2.4 Write a Python class, Flower, that has three instance variables of type
# str, int, and float, that respectively represent the name of the flower,
# its number of petals, and its price. Your class must include a constructor method
# that initializes each variable to an appropriate value, and your class should include
# methods for setting the value of each type, and retrieving the value of each type.


class Flower:
    ATTRIBUTE_NOT_SET = "Attribute not set"

    def __init__(self, name=None, petals=None, price=None) -> None:
        self.name = self.petals = self.price = None
        self.set_name(name)
        self.set_petals(petals)
        self.set_price(price)

    def set_name(self, name):
        if not name:
            raise ValueError("Invalid name, must be a non-empty string")
        else:
            self.name = name

    def set_petals(self, petals: int):
        if not petals or not isinstance(petals, int):
            raise ValueError("Invalid number, must be an integer")
        else:
            self.petals = petals

    def set_price(self, price):
        if not price:
            raise ValueError("Invalid price, must be a number (without currency sign)")
        else:
            self.price = price

    def get_name(self):
        if self.name:
            return self.name
        else:
            return Flower.ATTRIBUTE_NOT_SET

    def get_petals(self):
        if self.petals:
            return self.petals
        else:
            return Flower.ATTRIBUTE_NOT_SET

    def get_price(self):
        if self.price:
            return self.price
        else:
            return Flower.ATTRIBUTE_NOT_SET


rose = Flower(name="Rose", petals=1.2, price=12)
print(rose.get_name(), rose.get_petals(), rose.get_price())
