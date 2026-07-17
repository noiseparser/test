"""
Car Fleet: You are driving a car that starts at position 0 and travels at a constant speed towards target.
You are given an array of cars where each element is [position, speed], and you must return how many car fleets will arrive at destination.
"""


def carFleet(target: int, position: list[int], speed: list[int]) -> int:
    if not position:
        return 0

    cars = sorted(zip(position, speed), reverse=True)
    fleets = 0
    max_time = 0

    for pos, spd in cars:
        time = (target - pos) / spd
        if time > max_time:
            fleets += 1
            max_time = time

    return fleets


if __name__ == "__main__":
    assert carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]) == 3
    assert carFleet(10, [3], [3]) == 1
    assert carFleet(100, [0, 4, 2], [2, 1, 3]) == 1
