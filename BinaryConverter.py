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


# Note that all classes should store the decimal to ease in conversion

class Unsigned(Byte):
    lower_bound = 0
    upper_bound = 255

    def __init__(self, base_10: int):

        self.base_10 = base_10

        if self.lower_bound <= base_10 <= self.upper_bound:
            pattern_string = ""
            index_values = [128, 64, 32, 16, 8, 4, 2, 1]

            for value in index_values:
                if base_10 >= value:
                    pattern_string += "1"
                    base_10 -= value
                else:
                    pattern_string += "0"
            super().__init__(pattern_string)
        else:
            raise Exception("Unsigned integers can only support numbers from {} to {})".format(self.lower_bound, self.upper_bound))

    def negate(self):
        pass

    def to_base_10(self):
        # TODO: To be implemented
        return self.base_10

class Magnitude(Byte):
    lower_bound = -127
    upper_bound = 127

    def __init__(self, base_10: int):

        self.base_10 = base_10

        if self.lower_bound <= base_10 <= self.upper_bound:
            pattern_string = ""

            if base_10 < 0:
                pattern_string += "1"
                base_10 = abs(base_10)
            else:
                pattern_string += "0"

            index_values = [64, 32, 16, 8, 4, 2, 1]

            for value in index_values:
                if base_10 >= value:
                    pattern_string += "1"
                    base_10 -= value
                else:
                    pattern_string += "0"
            super().__init__(pattern_string)

        else:
            raise Exception("This type of signed integer can only support numbers from {} to {}".format(self.lower_bound, self.upper_bound))

    def negate(self):
        pass

    def to_base_10(self):
        # TODO: To be implemented
        return self.base_10


class Ones(Byte):
    lower_bound = -127
    upper_bound = 127

    def __init__(self, base_10: int):

        self.base_10 = base_10

        if self.lower_bound <= base_10 <= self.upper_bound:
            pattern_string = ""

            if base_10 < 0:
                pattern_string += "1"
                base_10 = abs(base_10)
            else:
                pattern_string += "0"

            index_values = [64, 32, 16, 8, 4, 2, 1]

            for value in index_values:
                if base_10 >= value:
                    pattern_string += "1"
                    base_10 -= value
                else:
                    pattern_string += "0"
            inverted_string = ""
            for bit in pattern_string:
                if bit == "0":
                    bit = "1"
                elif bit == "1":
                    bit = "0"
                inverted_string += bit

            super().__init__(inverted_string)

        else:
            raise Exception("This type of signed integer can only support numbers from {} to {}".format(self.lower_bound, self.upper_bound))

class Twos(Byte):
    lower_bound = -128
    upper_bound = 127

    def __init__(self, base_10: int):

        self.base_10 = base_10
        self.is_negative = False
        if self.base_10 < 0:
            self.is_negative = True
            self.base_10 *= -1
            self.base_10 += 1

        if self.lower_bound <= base_10 <= self.upper_bound:
            pattern_string = ""

            if base_10 < 0:
                pattern_string += "1"
                base_10 = abs(base_10)
            else:
                pattern_string += "0"

            index_values = [64, 32, 16, 8, 4, 2, 1]

            for value in index_values:
                if base_10 >= value:
                    pattern_string += "1"
                    base_10 -= value
                else:
                    pattern_string += "0"

            if self.is_negative:
                inverted_string = ""
                for bit in pattern_string:
                    if bit == "0":
                        bit = "1"
                    elif bit == "1":
                        bit = "0"
                    inverted_string += bit

                pattern_string = "1" + inverted_string[1:]

            super().__init__(pattern_string)

        else:
            raise Exception("This type of signed integer can only support numbers from {} to {}".format(self.lower_bound, self.upper_bound))

class Excess(Unsigned):
    def __init__(self, base_10: int):
        self.to_base_10

        super().__init__(base_10 + 128)

def convert(from_instance, to_class):
    return to_class(from_instance.to_base_10())

    def to_base_10(self):
        # TODO: To be implemented
        return self.base_10



# TESTS

print(Unsigned(73))
print(Magnitude(73))

print(Excess(73))
print(Excess(-73))

print(Ones(73))

print(Twos(73))
print(Twos(-73))
assert(Byte("11111111") == Unsigned(255))
assert(Unsigned(244) == convert(Unsigned(244), Unsigned))
