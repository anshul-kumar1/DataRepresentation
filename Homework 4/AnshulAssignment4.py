# Assignment 4 #

# Question 1
# converts the string into the corresponding ascii values
def string_to_ascii(inp: str) -> list:
    if not isinstance(inp, str):
        return [ValueError]
    final = []
    for char in inp:
        final.append(ord(char))
    return final

# test cases #
# print(string_to_ascii("hello"))
# print(string_to_ascii(""))
# print(123)


# converts the given ascii values into a string
def ascii_to_string(ascii_list: list) -> str:
    final = ""
    if len(ascii_list) == 0:
        return final

    for val in ascii_list:
        final = final + chr(val)

    return final

# Test cases #
# print(ascii_to_string([]))
# print(ascii_to_string([123,456,789]))
# print(ascii_to_string(string_to_ascii("hello")))

# Question 2
def string_to_unicode(inp: str) -> list:
    final = []
    for char in inp:
        final.append(ord(char))
    return final

def unicode_to_string(l: list) -> str:
    final = ""
    if len(l) == 0:
        return final
    for elem in l:
        if 0 <= elem <= 1114111:
            final = final + chr(elem)
        else:
            return 'Value Error'
    return final

print(unicode_to_string([1, 0, 0,123]))
# Question 3
def and_gate(input1: int, input2: int) -> int:
    # checking if it is a valid input and returning -1 if it is not
    if not (input1 == 1 or input1 == 0 and input2 == 1 or input2 == 0):
        return -1
    # only true case
    if input1 == 1 and input2 == 1:
        return 1

    return 0

# Test cases
# print(and_gate(1, 1))
# print(and_gate(1, 0))
# print(and_gate(0, 1))
# print(and_gate(0, 0))
# print(and_gate(5, 1))

def nor_gate(input1: int, input2: int) -> int:
    # checking if it is a valid input and returning -1 if it is not
    if not (input1 == 1 or input1 == 0 and input2 == 1 or input2 == 0):
        return -1
    # only true case
    if input1 == 0 and input2 == 0:
        return 1

    return 0

# Test cases
# print(nor_gate(1, 1))
# print(nor_gate(1, 0))
# print(nor_gate(0, 1))
# print(nor_gate(0, 0))
# print(nor_gate(5, 1))

# Question 5

# The equation for the given circuit is:
#       not ( (not (a or b or c)) and (a or b or c) and (a or (not b) or c) )
#       which is a tautology => it always yields true for all values of a,b,c
def complex_gate(a: int, b: int, c: int) -> int:
    if not ((a == 1 or a == 0) and (b == 1 or b == 0) and (c == 1 or c == 0)):
        return -1
    # The given circuit is a tautology
    return 1

# Test cases #
# print(complex_gate(1, 1, 1))
# print(complex_gate(0, 0, 0))
# print(complex_gate(1, 0, 0))
# print(complex_gate(1, 2, 1))
