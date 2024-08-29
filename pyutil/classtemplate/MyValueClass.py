class MyValueClass:

    __value : object

    def __init__(self, value: object):
        self.__value = value

    def __str__(self):
        return f"{self.__class__.__name__}={self.__value}"

    def __repr__(self):
        return self.__str__()

    def __hash__(self):
        return hash(self.__str__())

    def __lt__(self, obj):
        if not isinstance(obj, MyValueClass): return False
        return self.value < obj.value

    def __eq__(self, obj):
        if not isinstance(obj, MyValueClass): return False
        return self.value == obj.value

    def __ne__(self, obj):
        return not self.__eq__(obj)

    @property
    def value(self) -> object:
        return self.__value