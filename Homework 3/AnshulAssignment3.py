# Assignment 3 #

# Question 1 #
# logic: since the input is a string we can always check the first index to determine what the base of the value is
#           we can also find the other given formats
def read_change(inp: str):
    if inp[1] == 'b':
        print("The given input is binary")
        print("Decimal:", int(inp, 2))
        print("Octal:", oct(int(inp, 2)))
        print("Hexadecimal:", hex(int(inp, 2)))
    elif inp[1] == 'o':
        print("The given input is octal")
        print("Decimal:", int(inp, 8))
        print("Binary:", bin(int(inp, 8)))
        print("Hexadecimal:", hex(int(inp, 8)))
    elif inp[1] == 'x':
        print("The given input is hexadecimal")
        print("Decimal:", int(inp,16))
        print("Binary:", bin(int(inp,16)))
        print("Octal:", oct(int(inp,16)))
    else:
        print("The given input is decimal")
        print("Bin:", bin(int(inp)))
        print("Octal:", oct(int(inp)))
        print("Hexadecimal:", hex(int(inp)))

    return "-------------------------------------"

# Question 2
def evenout(bin1, bin2):
    if len(bin1) > len(bin2):
        displacement = len(bin1) - len(bin2)
        bin2 = "0" * displacement + bin2
        return bin1, bin2

    elif len(bin2) > len(bin1):
        displacement = len(bin2) - len(bin1)
        bin1 = "0" * displacement + bin1
        return bin1, bin2

# main helper function used to match both binary strings
def evenout_dec(bin1,bin2):
    if "." in bin1 and "." not in bin2:
        indexof = bin1.index('.')
        displacement = len(bin1) - indexof
        bin2 = bin2 + "." + ("0" * displacement)
        return bin1, bin2

    elif "." in bin2 and "." not in bin1:
        indexof = bin2.index('.')
        displacement = len(bin2) - indexof
        bin1 = bin1 + "." + ("0" * displacement)
        return bin1, bin2

    elif "." not in bin2 and "." not in bin1:
        if len(bin1) > len(bin2):
            displacement = len(bin1) - len(bin2)
            bin2 = "0" * displacement + bin2
            return bin1, bin2

        elif len(bin2) > len(bin1):
            displacement = len(bin2) - len(bin1)
            bin1 = "0" * displacement + bin1
            return bin1, bin2

    else:
        indexof_bin1 = bin1.index(".")
        indexof_bin2 = bin2.index(".")

        front_b1 = bin1[0:indexof_bin1]
        back_b1 = bin1[indexof_bin1:len(bin1)]

        front_b2 = bin2[0:indexof_bin2]
        back_b2= bin2[indexof_bin2:len(bin2)]

        bin1, bin2 = evenout(front_b1, front_b2)

        if back_b1 > back_b2:
            displacement = len(back_b1) - len(back_b2)
            back_b2 = back_b2 + displacement * "0"
            bin1 = bin1  + back_b1
            bin2 = bin2  + back_b2
            return bin1, bin2

        else:
            displacement = len(back_b2) - len(back_b1)
            back_b1 = back_b1 + displacement * "0"
            bin1 = bin1  + back_b1
            bin2 = bin2  + back_b2
            return bin1, bin2


def binary_sub_borrow(bin1: str, bin2: str) -> str:
    # checking for valid inputs
    if "." in bin1[2:len(bin1)] or "." in bin2[2:len(bin2)]:
        return ValueError
    if len(bin1) == 0 or len(bin2) == 0:
        return ValueError
    for i in bin1:
        if i != "0" and i != "1" and i != ".":
            return ValueError
    for i in bin2:
        if i != "0" and i != "1" and i != ".":
            return ValueError
    final = ""
    # ensuring both binary numbers are evened out
    bin1, bin2 = evenout_dec(bin1, bin2)
    # used ::-1 to loop through the list in reverse since subtraction is always done from left to right
    bin1 = bin1[::-1]
    bin2 = bin2[::-1]
    # intializing at 0 since we do not have a carry at the first
    borrow = 0
    for i, j in zip(bin1,bin2):
        if i != "." and j != ".":
            # changing the strings back to integers so we can work arithmitically
            num1_bit, num2_bit = int(i), int(j)
            # using 'temp' to iterate through the numbers while keeping track of the count
            temp = num1_bit - num2_bit - borrow
            # checking all possible cases
            if temp == 1:
                final = "1" + final
                borrow = 0
            elif temp == 0:
                final = "0" + final
                borrow = 0
            elif temp == -1:
                final = "1" + final
                borrow = 1
            elif temp == -2:
                final = "0" + final
                borrow = 1
        if i == "." and j == ".":
            final = "." + final
    return final

def two_compliment_subtraction(bin1, bin2):
    # checking for valid inputs
    if "." in bin1[2:len(bin1)] or "." in bin2[2:len(bin2)]:
        return ValueError
    if len(bin1) == 0 or len(bin2) == 0:
        return ValueError
    for i in bin1:
        if i != "0" and i != "1" and i != ".":
            return ValueError
    for i in bin2:
        if i != "0" and i != "1" and i != ".":
            return ValueError
    final = ""
    # ensuring both binary numbers are evened out
    bin1, bin2 = evenout_dec(bin1, bin2)
    one_comp, carry = "", 1
    for b in bin2:
        if b == '0':
            one_comp += '1'
        elif b == '1':
            one_comp += '0'
        elif b == '.':
            one_comp += '.'
    two_comp = ""
    # used ::-1 to loop through the list in reverse since subtraction is always done from left to right
    for i in one_comp[::-1]:
        if i != ".":
            # changing the strings back to integers so we can work arithmitically
            bin2_bit = int(i)
            temp = bin2_bit + carry
            if temp == 2:
                two_comp += "0"
                carry = 1
            elif temp == 1:
                two_comp += "1"
                carry = 0
            elif temp == 0:
                two_comp += "0"
                carry = 0
        else:
            two_comp += "."
    borrow = 0
    # used ::-1 to loop through the list in reverse since subtraction is always done from left to right
    bin1 = bin1[::-1]
    for i, j in zip(bin1,two_comp):
        if i == "." and j == ".":
            final = "." + final
        if i != "." and j != ".":
            # changing the strings back to integers so we can work arithmitically
            bin1_bit, bin2_bit = int(i), int(j)
            temp = bin1_bit + bin2_bit + borrow
            if temp == 2:
                final = "0" + final
                borrow = 1
            elif temp == 1:
                final = "1" + final
                borrow = 0
            elif temp == 0:
                final = "0" + final
                borrow = 0
            elif temp == 3:
                final = "1" + final
                borrow = 1

    return final
