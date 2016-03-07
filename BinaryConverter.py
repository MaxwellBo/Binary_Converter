class Byte(object):
    def __init__(self, pattern_string: str):
        self.pattern_dict = {}

        # So that 0 is the least significant bit
        # and to allow bit twiddling, this is a dictionary
        for index, char in enumerate(reversed(pattern_string)): 
            if char is '0':
                self.pattern_dict[index] = False
            elif char is '1':
                self.pattern_dict[index] = True

    def __repr__(self):
        string = ""
        for key in self.pattern_dict:
            if self.pattern_dict[key] is False:
                string += '0'
            elif self.pattern_dict[key] is True:
                string += '1'
        return "Byte(\"{}\")".format(string[::-1])

    def __eq__(self, other):
        return self.__repr__() == other.__repr__()


class Unsigned(Byte):
    def __init__(self, decimal: int):

        self.value = decimal

        if 0 <= decimal <= 255:
            pattern_string = ""
            index_values = [128, 64, 32, 16, 8, 4, 2, 1]

            for value in index_values:
                if decimal >= value:
                    pattern_string += "1"
                    decimal -= value
                else:
                    pattern_string += "0"
            super().__init__(pattern_string)
        else:
            raise Exception("Unsigned integers can only support numbers from 0 to 255")

class Magnitude(Byte):
    pass

class Ones(Byte):
    pass

class Twos(Byte):
    pass

class Excess(Byte):
    pass

def convert(from_instance, to_class):
    return to_class(from_instance.value)


# TESTS


assert(Byte("11111111") == Unsigned(255))
assert(Unsigned(244) == convert(Unsigned(244), Unsigned))
