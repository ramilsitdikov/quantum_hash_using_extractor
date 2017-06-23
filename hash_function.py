import sys
import math
import random

WORDSIZE = sys.getsizeof(5)


def random_set(size):
    '''
    :param size: number
    :return array of numbers
    '''
    array = []
    for i in range(size):
        n = random.randrange(1000)
        array.append(n)

    return array


def von_neuman_set(size):
    '''
    :param size: number
    :return array of numbers
    '''
    array = []
    acounter = 1
    for i in range(size):
        array.append(acounter)
        acounter *= 2

    return array


def von_neuman_extractor(message):
    '''
    :param message: number
    :return generated number based on message
    '''
    counter = 0
    bit_mask_array = [] # array of bit masks
    output_number = 0
    done = 0

    # initialize array
    bit_mask_array = random_set(WORDSIZE)

    for i in range(10):
        for counter in range(0, WORDSIZE, 2):
            if (message & bit_mask_array[counter]) ^ (message & bit_mask_array[counter + 1] >> 1):
                if counter > done:
                    output_number |= (message & bit_mask_array[counter]) >> (counter - done)
                elif counter < done:
                    output_number |= (message & bit_mask_array[counter]) << (done - counter)
                else:
                    output_number |= message & bit_mask_array[counter]
                done += 1
    return output_number


def new_hash_function(message, ring_size, t_param):
    '''
    :param message: number
    :param ring_size: size of set(ring)
    :param t_param: size parameters set
    :return hashed message
    '''
    result = 0
    for i in range(t_param):
        result += math.cos(2 * math.pi * von_neuman_extractor(message))
    result = result / t_param


    return math.fabs(result)

if __name__ == "__main__":
    message = 11
    hashed_message = new_hash_function(message, 10, WORDSIZE)
    print("message =", message)
    print("hashed_message =", hashed_message)