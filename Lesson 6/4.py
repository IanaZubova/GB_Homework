class Car:
    direction = None

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return ("Car drives")

    def stop(self):
        return ("Car stopped")

    def turn(self, direction):
        if direction == 'right':
            return (f"Car turned right")
        else:
            direction == 'left'
            return (f"Car turned left")

    def show_speed(self):
        return (f"Speed: {self.speed}")

    def show_name(self):
        return (self.name)


class TownCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            print(f"Warning: unallowed speed")
        else:
            print(f"Speed is ok")


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            print(f"Warning: unallowed speed")
        else:
            print(f"Speed is ok")


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


mini = TownCar(80, 'metallic', 'Mini', False)
bmw = SportCar(120, 'black', 'BMW', False)
bus = WorkCar(40, 'white', 'Bus', False)
ford = PoliceCar(100, 'blue', 'Ford', True)

print(mini.show_speed())
print(bus.show_speed())
print(ford.go())
print(ford.turn('left'))