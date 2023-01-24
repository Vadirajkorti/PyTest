class Fruit(object):
    def __init__(self, vitamin, shape):
        self.shape = shape
        self.vitamin = vitamin

    def nutrition(self):
        print(f"It has vitamin {self.vitamin}")

    def fruit_shape(self):
        print(f"The shape of fruit is {self.shape}")


class Orange(Fruit):
    def __init__(self, vitamin, shape):
        # super().__init__(vitamin, shape)
        Fruit.__init__(self, vitamin, shape)

    def nutrition(self):
        print(f"Orange has {self.vitamin}")

    def fruit_shape(self):
        print(f"The shape of Orange is {self.shape}")


o = Orange("Vit C", "round")

o.nutrition()
o.fruit_shape()
