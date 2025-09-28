class CarPark:
    def __init__(self, id_, count=0):
        self.id_ = id_
        self.count = count
        self.cars = []

    def __add__(self, other):
        self.cars.append(other)
        self.count += 1
        return self

    def __len__(self):
        return len(self.cars)

    def __eq__(self, other):
        try:
            return len(self) == len(other)
        except TypeError:
            return "Oops: one of carparks is clear."

    def __str__(self):
        return f"CarPark №{self.id_}, there is {self.count} auto: {[str(x) for x in self.cars]}"
