"""
Solution for Day 4 of Advent of Code 2018.

Problem: Repose Record

Part 1: What is the ID of the guard (slept the most minutes in all shifts)
you chose multiplied by the minute you chose?

Part 2: What is the ID of the guard (slept most frequently on some minute)
you chose multiplied by the minute you chose?

Side notes: this is by far the trickiest challenge out of the 4 days so far...
Code is not the best but gets the job done *face palm*

For more details of what the problems were, go to https://adventofcode.com/2018/
"""

import re
from collections import Counter, defaultdict


def day4_solutions():
    # This is what I'm trying to match:
    # [1518-05-30 00:04] Guard #2417 begins shift
    event_re = re.compile(r"\[.+?(\d+-\d+) (?:\d+:)(\d+)\] (.+?(\d+).+|wakes up|falls asleep)")
    with open("day4.txt") as input_f:
        events = sorted(line.strip() for line in input_f)
    events = [event_re.search(event).groups() for event in events]

    events_log = []
    # Temporary buffer variables for building up the event log for a day
    day_log = {"mins": set()}
    minute_begin = 0
    minute_end = 0

    for i, (date, minute, event, guard_id) in enumerate(events):
        if "date" not in day_log:
            day_log["date"] = date

        if guard_id is not None:
            if i > 0:
                # Beginning of a new day (and it's not the first event), so add the record built
                # from prev day first
                day_log["mins_slept"] = len(day_log["mins"])
                events_log.append(day_log)
            # ... before clearing it
            day_log = {"mins": set()}
            # Then set the ID to today's guard
            day_log["id"] = int(guard_id)
            continue
        else:
            # No guard id found, so must be a wake up or asleep event
            if event == "falls asleep":
                minute_begin = int(minute)
            else:
                minute_end = int(minute)
                # Now that we know when the guard started and stopped sleeping,
                # we can fill in the gaps
                for minute in range(minute_begin, minute_end):
                    day_log["mins"].add(minute)

    # Final append required to capture the final day's activity as there are no more
    # new shifts event which would have triggered the append
    day_log["mins_slept"] = len(day_log["mins"])
    events_log.append(day_log)

    total_sleep_times = defaultdict(lambda: {"mins_slept": 0, "counts": []})
    for day_log in events_log:
        # day_log = {"date": ..., "id": ..., "mins": ..., "mins_slept": ...}
        # day_log["id"] = guard ID
        total_sleep_times[day_log["id"]]["mins_slept"] += day_log["mins_slept"] 
        for min_ in day_log["mins"]:
            total_sleep_times[day_log["id"]]["counts"].append(min_)

    sleepiest_guard = sorted(total_sleep_times.items(), key=lambda t: t[1]["mins_slept"], reverse=True)[0][0]
    (most_asleep_min, _), = Counter(total_sleep_times[sleepiest_guard]["counts"]).most_common(1)
    part1 = sleepiest_guard * most_asleep_min

    # Part 2
    total_sleep_times = {k: Counter(v["counts"]).most_common(1)
                         for k, v in total_sleep_times.items() if v["counts"]}
    sleepiest_guard, ((most_asleep_min, _),) = sorted(
        total_sleep_times.items(), key=lambda t: t[1][0][1], reverse=True)[0]
    part2 = sleepiest_guard * most_asleep_min
    return part1, part2


if __name__ == '__main__':
    print("=" * 15, "Part 1", "=" * 15)
    part1, part2 = day4_solutions()
    print(f"The answer is {part1}")

    print()
    print("=" * 15, "Part 2", "=" * 15)
    print(f"The answer is {part2}")
