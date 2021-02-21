mass_for_m2 = 25
sm = 5

class Road:

    def __init__(self, lenght, width):
        self.__lenght = lenght
        self.__width = width

    def calculation(self):
        return self.__lenght * self.__width * mass_for_m2 * sm


result = Road(10, 200)
print(f"Total bitum mass: {result.calculation()}")