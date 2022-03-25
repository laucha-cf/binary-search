from binary import binary_search, recursive_binary_search
from sequential_search import sequential_search
import random
import time
import os


if __name__ == '__main__':
    length = int(input('Put the length of the list >> '))
    sorted_list = set()
    for n in range(length):
        sorted_list.add( random.randint( -3*length, 3*length ) )

    sorted_list = sorted( list(sorted_list) )

    f = open('results.txt', 'a')
    sequential_time = 0
    binary_time = 0
    rec_binary_time = 0

    for i in range(length):
        target = random.choice( sorted_list )
        start = time.time()
        sequential_search(sorted_list,target)
        end = time.time()
        sequential_time += end - start

        start = time.time()
        binary_search(sorted_list,target)
        end = time.time()
        binary_time += end - start

        start = time.time()
        recursive_binary_search(sorted_list,target)
        end = time.time()
        rec_binary_time += end - start
        


    f.write(f'Sequential Search       -> {sequential_time} seconds \n')

    f.write(f'(Recursive)Binary Search-> {rec_binary_time} seconds \n')

    f.write(f'Binary Search           -> {binary_time} seconds \n\n')

    f.close()








