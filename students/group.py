class Group:
    def __init__(self, id_):
        self.id_ = id_
        self.students = []

    def __add__(self, st):
        st.group = self.id_
        self.students.append(st)
        return self

    def __str__(self):
        return f"group id = {self.id_}, students is here: {[str(x) for x in self.students]}"

    def __len__(self):
        return len(self.students)

    def __eq__(self, gr2):
        return len(self) == len(gr2)
