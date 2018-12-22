"""
Solution for Day 1 of Advent of Code 2018.

Problem: Chronal Calibration

Part 1: What is the resulting frequency after all changes of frequency (from input file)
has been applied?

Part 2: What is the first frequency your device reaches twice?

For more details of what the problems were, go to https://adventofcode.com/2018/
"""

def get_resulting_frequency():
    with open("day1.txt") as input_f:
        changes = (int(line.strip()) for line in input_f)
        return sum(changes)

def get_first_repeated_frequency():
    seen = {0}
    current_frequency = 0
    with open("day1.txt") as input_f:
        while True:
            line = input_f.readline().strip()
            if line:
                current_frequency += int(line)
                if current_frequency not in seen:
                    seen.add(current_frequency)
                else:
                    # We've seen this before, return!
                    return current_frequency
            else:
                # We reached EOF, so reset cursor to beginning of file before carrying on
                input_f.seek(0)

if __name__ == '__main__':
    print("=" * 15, "Part 1", "=" * 15)
    result = get_resulting_frequency()
    print(f"The resulting frequency is {result}")
    
    print()
    print("=" * 15, "Part 2", "=" * 15)
    print(f"The first repeated frequency is {get_first_repeated_frequency()}")
