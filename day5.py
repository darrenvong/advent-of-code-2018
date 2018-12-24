"""
Solution for Day 5 of Advent of Code 2018.

Problem: Alchemical Reduction

Part 1: How many units remain after fully reacting the polymer you scanned?

Part 2: What is the length of the shortest polymer you can produce
by removing all units of exactly one type and fully reacting the result?

For more details of what the problems were, go to https://adventofcode.com/2018/
"""

import string

UPPERCASE = "upper"
LOWERCASE = "lower"

def get_case(element):
    return UPPERCASE if element.isupper() else LOWERCASE

def get_remained_units(polymer):
    reaction_chain = []
    for element in polymer:
        if not reaction_chain:
            # The chain is empty, so just add the current element on as there's nothing else to
            # react with
            reaction_chain.append(element)
        else:
            # Chain not empty...
            head = reaction_chain[-1]
            # So first check if the "head" element has opposite polarity and if they are the same letter
            if get_case(head) != get_case(element) and head.lower() == element.lower():
                # Since that's the case, a reaction occurs so remove the head element
                reaction_chain.pop()
            else:
                # No reaction happens, so keep adding it to the chain
                reaction_chain.append(element)

    return len(reaction_chain)

def get_shortest_polymer_length(polymer):
    lengths = []
    for element in string.ascii_lowercase:
        filtered_polymer = filter(lambda e: e.lower() != element, polymer)
        lengths.append(get_remained_units(filtered_polymer))
    return min(lengths)

if __name__ == '__main__':
    print("=" * 15, "Part 1", "=" * 15)
    with open("day5.txt") as input_f:
        polymer = input_f.read().strip()
    units = get_remained_units(polymer)
    print(f"{units} units remained after the reaction.")

    print()
    print("=" * 15, "Part 2", "=" * 15)
    shortest_length = get_shortest_polymer_length(polymer)
    print(f"The length of the shortest polymer is {shortest_length}.")
