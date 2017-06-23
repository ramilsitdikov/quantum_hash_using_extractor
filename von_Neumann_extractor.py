# von Neumann extractor
print("Work begins")

import numpy as np
import ctypes
import sys
WORDSIZE = sys.getsizeof(5)

print("size of int =", sys.getsizeof(int))
print("size of 1 =", sys.getsizeof(1))
print("size of 5 =", sys.getsizeof(5))


# init
counter = 0
bit_mask_array = [] # array of bit masks
output_number = 0
done = 0
acounter = 1

# initialize array
for counter in range(WORDSIZE):
    bit_mask_array.append(acounter)
    acounter *= 2

print("WORDSIZE =", WORDSIZE)

input_number = int(raw_input(">> "))
for i in range(10):
    for counter in range(0, WORDSIZE, 2):
        if ((input_number & bit_mask_array[counter])) ^ ((input_number & bit_mask_array[counter + 1]) >> 1):
            if (counter > done):
                output_number |= ((input_number & bit_mask_array[counter]) >> (counter-done))
            elif (counter < done):
                output_number |= ((input_number & bit_mask_array[counter]) << (done-counter))
            else:
                output_number |= (input_number & bit_mask_array[counter])
            done += 1
            print("output_number =", output_number)
            print("DONE =", done)

            if (done == WORDSIZE):
                print("output_number =", output_number)
                output_number = 0
                done = 0
    # input_number = int(raw_input(">> "))


print("Work is done")