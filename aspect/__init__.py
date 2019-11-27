class Aspect:
"""
Class representing categorical value, default value is always of index 0 from values_list
"""
    def __init__(self, values_list):
        self.__values = values_list
        self.__value = self.__values[0]


    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        if value in self.__values:
            self.__value = value
        else:
            raise ValueError("value {} is not in allowed values".format(value))

    