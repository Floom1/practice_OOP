import abc


class Aggregate(abc.ABC):
    @abc.abstractmethod
    def iterator(self):
        pass


class Iterator(abc.ABC):
    def __init__(self, collection, cursor):
        self._collection = collection
        self._cursor = cursor

    @abc.abstractmethod
    def first(self):
        pass

    @abc.abstractmethod
    def next(self):
        pass

    @abc.abstractmethod
    def current(self):
        pass
