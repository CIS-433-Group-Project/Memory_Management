from Page_Replacement import MemoryManager, Strategy
from Reference_String import generate_list, Behavior
from csv import DictReader, DictWriter
from time import time
from operator import itemgetter


def test_behavior_strategy(b: Behavior, s: Strategy, size=20):
    TRIALS = 10**2
    results = []
    start = time()
    dynamic = False
    for _ in range(TRIALS):
        r = MemoryManager(s, size, dynamic).handle_string(generate_list(b))
        results.append(r)
    end = time()
    avg_time = (end - start)/TRIALS
    print('Average time: ', avg_time)
    print('Minimum no. page faults: ', min(results))
    print('Maximum no. page faults: ', max(results))
    avg = sum(results)/len(results)
    print('Average no. page faults: ', avg)
    with open('benchmarks.csv', 'r') as record_file:
        data = DictReader(record_file)
        entries = [i for i in data]
    entry_fields = ['Behavior', 'Strategy', 'Res. Set Size', 'Faults']
    new_entry = {'Behavior': b.name, 'Strategy': s.name, 'Res. Set Size': size, 'Faults': int(avg)}
    entries.append(new_entry)
    entries = sorted(entries, key=itemgetter('Behavior'))
    with open('benchmarks.csv', 'w', newline='') as record_file:
        writer = DictWriter(record_file, entry_fields)
        writer.writeheader()
        writer.writerows(entries)


if __name__ == '__main__':
    test_behavior_strategy(Behavior.LOOP, Strategy.LRU)
