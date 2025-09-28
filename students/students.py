class Student:
    def __init__(self, id_, name, second_name, group=0):
        self.name = name
        self.second_name = second_name
        self.id_ = id_
        self.group = group

    def __str__(self):
        return f"student with id = {self.id_} is {self.name} {self.second_name} from group {self.group}"
