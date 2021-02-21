class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Start drawing")


class Pen(Stationery):

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print("Start drawing by pen")


class Pencil(Stationery):

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print("Start drawing by pencil")


class Marker(Stationery):

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print("Start drawing by marker")


pen = Pen('pen')
pencil = Pencil('pencil')
marker = Marker('marker')

print(pen.draw())
print(pencil.draw())
print(marker.draw())