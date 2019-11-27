class Aspect:
"""
Class representing categorical value
"""
    def __init__(self, values_list):
        self.__values = set(values_list)
        self.__value = self.__values[0]

    @property
    def values(self):
        return self.__values

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        if value in self.__values:
            self.__value = value
        else:
            raise ValueError("value {} is not in allowed values".format(value))

    def __hash__(self):
        return hash(tuple(list(self.__values)))

    def __eq__(self, other):
        return hash(self) == hash(other) and self.value == other.value


    