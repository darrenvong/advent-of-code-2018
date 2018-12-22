"""
Solution for Day 2 of Advent of Code 2018.

Problem: Inventory Management System

Part 1: What is the checksum for my list of box IDs?

Part 2: What letters are common between two correct box IDs?

Hamming distance is a good algorithm to use since part 2 essentially is a task of finding which
two words has distance 1, before identifying which letter caused the distance.

For more details of what the problems were, go to https://adventofcode.com/2018/
"""

from collections import Counter

def get_checksum():
    with open("day2.txt") as input_f:
        counts = [Counter(line.strip()) for line in input_f]
        counts_with_two_letters = list(filter(lambda c: 2 in c, (counter.values() for counter in counts)))
        counts_with_three_letters = list(filter(lambda c: 3 in c, (counter.values() for counter in counts)))
        return len(counts_with_two_letters) * len(counts_with_three_letters)

def hamming_distance(s1, s2):
    """Return the Hamming distance between equal-length sequences, and the letter pairs used
    to calculate the distance that will be useful for finding which letter differed.
    (modified from Wikipedia code)."""
    if len(s1) != len(s2):
        raise ValueError("Undefined for sequences of unequal length")
    letter_pairs = [el1 != el2 for el1, el2 in zip(s1, s2)]
    return sum(letter_pairs), letter_pairs

def get_common_letters():
    with open("day2.txt") as input_f:
        box_ids = [line.strip() for line in input_f]

        for id1 in box_ids:
            for id2 in box_ids[1:]:
                dist, letter_pairs = hamming_distance(id1, id2)
                if dist == 1:
                    # The index of where "True" is where the position of the differing
                    # letter is
                    diff_index = letter_pairs.index(True)
                    # Returns the remaining string with the differing letter removed as required
                    return id1[0:diff_index] + id1[diff_index + 1:]


if __name__ == '__main__':
    print("=" * 15, "Part 1", "=" * 15)
    result = get_checksum()
    print(f"The checksum is {result}")
    
    print()
    print("=" * 15, "Part 2", "=" * 15)
    print(f"The letters in common are {get_common_letters()}")
