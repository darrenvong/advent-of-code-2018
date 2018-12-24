"""
Solution for Day 6 of Advent of Code 2018.

Problem: Chronal Coordinates

Part 1: What is the size of the largest area that isn't infinite?

Part 2: What is the size of the region containing all locations
which have a total distance to all given coordinates of less than 10000?

Another toughie after day 4... Looks like I missed a trick by not realising points
near the edge of grid is infinite, and so any near the edge marked with those points
can be ruled out. Not sure how much time (both coding and running) that would have
saved, if I had implemented the idea in my code.

This is by far the ugliest solution I've done... what a contrast compared to that of
day 5's!!!

For more details of what the problems were, go to https://adventofcode.com/2018/
"""

from collections import Counter, defaultdict
from functools import reduce

UNDEFINED = -1
EQUIDIST = -2

def manhattan_distance(p1, p2):
    return abs(p2[0] - p1[0]) + abs(p2[1] - p1[1])

# Ugly, but don't really know how to make it cleaner tbh...
def part2(points, limit, grid):
    for x in range(40, limit):
        for y in range(40, limit):
            if grid[x][y] != UNDEFINED:
                continue

            distances = sum(manhattan_distance(point, (x, y)) for point in points)
            grid[x][y] = distances
    
    dist_sums = [dist for ys in grid.values() for dist in ys.values() if dist < 10000]
    return len(dist_sums)


def generate_grid(points, limit, grid):
    for x in range(limit):
        for y in range(limit):
            if grid[x][y] != UNDEFINED:
                continue

            distances = [manhattan_distance(point, (x, y)) for point in points]
            min_dist = min(distances)
            dist_counts = Counter(distances)

            # set grid[x][y] to argmin
            grid[x][y] = distances.index(min_dist) if dist_counts[min_dist] == 1 else EQUIDIST
    
    id_counts = [Counter(ys.values()) for ys in grid.values()]
    master_counter = reduce(lambda acc, next: acc.update(next) or acc, id_counts, Counter())

    return set(master_counter.values())

def get_largest_area(points, start, limit_max, step):
    
    # Generate grid - probably best to refactor in function later
    grid = defaultdict(lambda: defaultdict(lambda: UNDEFINED))
    simulations = [generate_grid(points, limit, grid) for limit in range(start, limit_max, step)]

    converged_set = reduce(lambda l, r: l & r, simulations)
    return max(converged_set)


if __name__ == '__main__':
    print("=" * 15, "Part 1", "=" * 15)
    with open("day6.txt") as input_f:
        points = [tuple(map(int, line.strip().split(", "))) for line in input_f]
    print(f"The largest finite area is {get_largest_area(points, 500, 600, 50)}")

    print()
    print("=" * 15, "Part 2", "=" * 15)
    grid = defaultdict(lambda: defaultdict(lambda: UNDEFINED))
    dist_sums = part2(points, 370, grid)
    print(f"The size of the region where all points have dist < 10000 is {dist_sums}")
