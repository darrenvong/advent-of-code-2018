"""
Solution for Day 3 of Advent of Code 2018.

Problem: No Matter How You Slice It

Part 1: How many square inches of fabric are within two or more claims?

Part 2: What is the ID of the only claim that doesn't overlap?

For more details of what the problems were, go to https://adventofcode.com/2018/
"""

import re
from collections import Counter, defaultdict

def day3_solutions():
    claim_re = re.compile(r"#\d+\s@\s(\d+),(\d+):\s(\d+)x(\d+)")
    rect = defaultdict(lambda: defaultdict(lambda: "."))
    with open("day3.txt") as input_f:
        claims_data = [tuple(map(int, claim_re.search(line).groups())) for line in input_f]
        for claim_id, (x, y, width, height) in enumerate(claims_data, 1):

            for i in range(x, x + width):
                for j in range(y, y + height):
                    if rect[i][j] == "x":
                        # Overlapped square, so no need to mark it again
                        continue
                    elif rect[i][j] == ".":
                        # Fresh square, so mark it with current claim number
                        rect[i][j] = claim_id
                    else:
                        # Used square, so mark with "x" to indicate overlap
                        rect[i][j] = "x"
    
    markers_it = (ys.values() for ys in rect.values())
    counts = (Counter(markers) for markers in markers_it)

    claims_area = defaultdict(int)
    for count in counts:
        for claim_id, num_occupied in count.items():
            claims_area[claim_id] += num_occupied
    
    # part 2
    unique_id = 0
    for claim_id, area in claims_area.items():
        if claim_id == "x":
            continue
        x, y, width, height = claims_data[claim_id - 1]
        if width * height == area:
            unique_id = claim_id
            break

    return claims_area["x"], unique_id

if __name__ == '__main__':
    print("=" * 15, "Part 1", "=" * 15)
    overlapped_area, unique_id = day3_solutions()
    print(f"The answer is {overlapped_area}")
    
    print()
    print("=" * 15, "Part 2", "=" * 15)
    # non overlapped ID
    print(f"The unique ID is {unique_id}")
