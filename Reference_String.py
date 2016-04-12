from random import randint, choice
from enum import Enum
from time import time


class Behavior(Enum):
    RANDOM = 1
    WELLBEHAVED = 2
    TERRIBLE = 3
    AVERAGE = 4
    LOOP = 5


def generate_list(behavior: Behavior, loop_len=None):
    LENGTH = 10**4
    RANGE = 99
    if behavior == Behavior.RANDOM:
        l = range(RANGE+1)
        ref = [choice(l) for _ in range(LENGTH)]
    else:
        ref = [None for _ in range(LENGTH)]
        pages = [i for i in range(RANGE+1)]
        if behavior == Behavior.LOOP:
            if loop_len is None:
                loop_len = randint(3, 12)
            start = randint(0, RANGE)
            loop = []
            for i in range(loop_len):
                loop.append(pages[(start + i) % len(pages)])
            loop_iterations = int(LENGTH*randint(7, 9)/10/len(loop))
            for i in loop:
                pages.remove(i)
            loop_start = randint(0, LENGTH - len(loop)*loop_iterations - 1)
            for i in range(len(loop)*loop_iterations):
                ref[loop_start + i] = loop[i % len(loop)]
            p = pages.copy()
            for i in range(LENGTH):
                if len(p) == 0:
                    p = pages.copy()
                if ref[i] is None:
                    ref[i] = p.pop(randint(0, len(p)-1))
            assert set(pages).union(loop) == {i for i in range(RANGE+1)}
            assert loop_iterations*len(loop) + len(pages) <= LENGTH
            assert all(i is not None for i in ref)
            assert all(i in ref for i in range(100))
    return ref


if __name__ == '__main__':
    TRIALS = 10**2
    time_start = time()
    for _ in range(TRIALS):
        n = generate_list(Behavior.LOOP)
    time_end = time()
    print('Time elapsed: ', time_end - time_start)
    print('Average time: ', (time_end - time_start)/TRIALS)
    with open('test_string_loop.txt', 'w') as file_out:
        file_out.write(', '.join([str(i) for i in n]))

