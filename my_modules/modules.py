class Car:
    """ Car Class """
    # Car Atributes
    __brand = "hello"
    model = ""
    colour = ""

    # Constructor
    def __init__(self, brand, model, colour):
        self.__brand = brand
        self.model = model
        self.colour = colour

    # Method to Get Car
    def get_car(self):
        print(f'This is a {self.colour} coloured {self.__brand} {self.model}')
