from IteratorABC import Iterator, Aggregate

class ListIterator(Iterator):
    def __init__(self, collection, cursor):
        super().__init__(collection, cursor)

    def first(self):
        self._cursor = -1

    def next(self):
        if self._cursor + 1 >= len(self._collection):
            raise StopIteration()
        self._cursor += 1

    def current(self):
        return self._collection[self._cursor]

class ListCollection(Aggregate):
    def __init__(self, collection):
        self._collection = list(collection)

    def iterator(self):
        return ListIterator(self._collection, -1)


col = (1, 3, 123 , 1 , 2 , 3 ,99)

aggregate = ListCollection (col)
itr = aggregate.iterator()

while True:
    try:
        itr.next()
    except StopIteration:
        break
    print(itr.current())

itr.first()
print("\n\n")
while True:
    try:
        itr.next()
    except StopIteration:
        break
    print(itr.current())
