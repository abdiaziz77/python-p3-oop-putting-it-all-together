class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size
        self.condition = "Used"

    def get_brand(self):
        return self._brand

    def set_brand(self, value):
        if isinstance(value, str):
            self._brand = value
        else:
            print("Brand must be a string.")

    brand = property(get_brand, set_brand)

    def get_size(self):
        return self._size

    def set_size(self, value):
        if isinstance(value, int):
            self._size = value
        else:
            print("size must be an integer")

    size = property(get_size, set_size)

    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"
