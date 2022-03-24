from binary import binary_search, recursive_binary_search
from sequential_search import sequential_search
import random
import time
import os


if __name__ == '__main__':
    length = 100000
    sorted_list = set()
    for n in range(length):
        sorted_list.add( random.randint( -3*length, 3*length ) )

    sorted_list = sorted( list(sorted_list) )

    f = open('results.txt', 'a')

    start = time.time()
    for target in sorted_list:
        sequential_search(sorted_list, target)
    end = time.time()
    f.write(f'Sequential Search       -> {(start+end) / 2} seconds \n')

    start = time.time()
    for target in sorted_list:
        recursive_binary_search(sorted_list, target)
    end = time.time()
    f.write(f'(Recursive)Binary Search-> {(start+end) / 2} seconds \n')

    start = time.time()
    for target in sorted_list:
        binary_search(sorted_list, target)
    end = time.time()
    f.write(f'Binary Search           -> {(start+end) / 2} seconds \n\n')








