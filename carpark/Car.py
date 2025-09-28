class Car:
    def __init__(self, mark, year):
        self.mark = mark
        self.year = year

    def __str__(self):
        return f"Марка - {self.mark}, Год выпуска - {self.year}"
