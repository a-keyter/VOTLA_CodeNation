import random
import time

#function starts as binary and turns into inputed text
def binary_text(string):
    length = len(string)
    binary = ""
    #creates binary digits
    for i in range(length):
        one_zero = random.randint(0, 1)
        binary += str(one_zero)
    print(binary, end="\r")

    output = ""
    #loop changes 1 binary digit to a letter at a time
    for i in range(length):
        time.sleep(0.4)

        #turns string to list
        binary = list(binary)

        #changes the binary digit to letter from string
        binary[i] = string[i]

        output = ""

        #turns list to string
        for k in range(length):
            output += binary[k]

        #prints output, deletes line after printed unless it is finished output
        if i == (length - 1):
            print(output)
        else:
            print(output, end="\r")

print("Hello World!")
time.sleep(0.5)
binary_text('Hello World!')