from random import randint, choice, random
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
    ref = []
    # Random program behavior.  Only guarantees that ref[i] != ref[i+1].
    if behavior == Behavior.RANDOM:
        app = ref.append
        l = range(RANGE+1)
        last = None
        for _ in range(LENGTH):
            c = choice(l)
            while c == last:
                c = choice(l)
            last = c
            app(c)
    # Implementation of average program behavior.  Assumes average programs simply adhere to the 90-10 rule.
    elif behavior == Behavior.AVERAGE:
        ref = [None]*LENGTH
        ws = range(RANGE+1)
        working_set = []
        while len(working_set) < 10:
            working_set = {choice(ws) for _ in range(len(ws)//10)}
        working_set = list(working_set)
        leftovers = [i for i in ws if i not in working_set]
        ref[0] = choice(leftovers)
        ref[-1] = choice(working_set)
        for i in range(1, len(ref)-1):
            placement = random()
            before = ref[i - 1]
            after = ref[i + 1]
            while ref[i] == before or ref[i] == after or not ref[i]:
                if placement > 0.9:
                    ref[i] = choice(leftovers)
                else:
                    ref[i] = choice(working_set)
        assert all(ref[i] != ref[i + 1] for i in range(len(ref) - 1))
        assert all(i is not None for i in ref)
        uses = {i: sum([1 if i == j else 0 for j in ref]) for i in working_set}

        return ref
    # Implementation of Loop behavior.
    else:
        ref = [None]*LENGTH
        pages = [i for i in range(RANGE+1)]
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
        assert all(ref[i] != ref[i+1] for i in range(len(ref)-1))
    return ref


if __name__ == '__main__':
    TRIALS = 10**2
    time_start = time()
    for _ in range(TRIALS):
        n = generate_list(Behavior.AVERAGE)
    time_end = time()
    print('Time elapsed: ', time_end - time_start)
    print('Average time: ', (time_end - time_start)/TRIALS)
    with open('test_string_loop.txt', 'w') as file_out:
        file_out.write(', '.join([str(i) for i in n]))

