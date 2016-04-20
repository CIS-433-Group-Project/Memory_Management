from enum import Enum
from collections import deque
from random import choice
from operator import itemgetter


class Strategy(Enum):
        FIFO = 0
        LRU = 1
        LRUA = 2
        OPTIMAL = 3
        RANDOM = 4


class MemoryManager:
    def __init__(self, s: Strategy, free_size: int, dynamic=False):
        self.size = free_size
        self.strategy = s
        self.static_size = not dynamic

    def handle_string(self, ref: list, size_limit=0):
        LENGTH = len(ref)
        if self.static_size:
            size_limit = self.size
        elif size_limit < self.size:
            size_limit = 10**4
        total_faults = 0
        working_set = deque()
        recent_faults = deque(maxlen=size_limit)
        position = 0
        for i in ref:
            fault = i not in working_set
            recent_faults.append(fault)
            if fault:
                total_faults += 1
                if not self.static_size and len(recent_faults) >= self.size:
                    if sum(recent_faults)/len(recent_faults) >= 0.5 and self.size < size_limit:
                        self.size += 1
                    elif sum(recent_faults) == 0:
                        self.size -= 1
                # Strategy handling happens here.
                if len(working_set) == self.size:
                    # FIFO:  just remove the left-most element of the working set.
                    if self.strategy == Strategy.FIFO:
                        working_set.popleft()
                    # Random strategy:  just remove an element at random.
                    if self.strategy == Strategy.RANDOM:
                        working_set.remove(choice(working_set))
                    # LRU:  Remove the element which was least recently used - that is, the one which is farthest left
                    # in the reference string from this position.
                    if self.strategy == Strategy.LRU:
                        # ref_slice = ref[:position]
                        # ref_slice.reverse()
                        # recent_page_positions = [(ref_slice.index(i), i) for i in working_set]
                        # working_set.remove(max(recent_page_positions, key=itemgetter(0))[1])
                        working_set.popleft()
                    # Optimal page replacement - remove the page which will be used the farthest in the future from
                    # here.
                    # Gets a slice of the rest of the reference string, creates a list of tuples containing the page
                    # number and the next index within our reference string where that page appears.  The page number
                    # associated with the largest index is the one we drop.
                    if self.strategy == Strategy.OPTIMAL:
                        ref_slice = ref[position:]
                        future_positions = [(ref_slice.index(i) if i in ref_slice else LENGTH, i)
                                            for i in working_set]
                        # this max returns a tuple, of which we only need the 2nd element, hence the indexing.
                        furthest = max(future_positions, key=itemgetter(0))[1]
                        working_set.remove(furthest)
                working_set.append(i)
            elif self.strategy == Strategy.LRU:
                working_set.remove(i)
                working_set.append(i)
            position += 1
        return total_faults


if __name__ == '__main__':
    m = MemoryManager(Strategy.LRU, 20)
    with open('test_string_loop.txt', 'r') as filein:
        test_ref = filein.read().split(', ')
    print(m.handle_string(test_ref))

