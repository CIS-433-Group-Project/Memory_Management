from Page_Replacement import MemoryManager, Strategy
from Reference_String import generate_list, Behavior
from time import time


def test_behavior_strategy(b: Behavior, s: Strategy):
    TRIALS = 10**3
    results = []
    start = time()
    dynamic = False
    for _ in range(TRIALS):
        results.append(MemoryManager(s, 10, dynamic).handle_string(generate_list(b), 15))
    end = time()
    avg_time = (end - start)/TRIALS
    print('Average time: ', avg_time)
    print('Minimum no. page faults: ', min(results))
    print('Maximum no. page faults: ', max(results))
    avg = sum(results)/len(results)
    print('Average no. page faults: ', avg)
    with open('benchmarks.txt', 'r') as record_file:
        data = [line.strip() for line in record_file]
    new_entry = b.name + " string generation, "
    new_entry += s.name + ' replacement'
    if not dynamic:
        new_entry += ', STATIC size:'
    else:
        new_entry += ':'
    new_entry += '\t' + str(int(avg)) + ' faults.'
    count = 0
    for line in data:
        if line.startswith(b.name) and s.name in line:
            break
        count += 1
    data.insert(count, new_entry)
    with open('benchmarks.txt', 'w') as record_file:
        record_file.write('\n'.join(data))


if __name__ == '__main__':
    test_behavior_strategy(Behavior.LOOP, Strategy.FIFO)


