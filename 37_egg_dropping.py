def minimum_egg_drops(eggs, floors):
    reachable = [0] * (eggs + 1)
    moves = 0

    while reachable[eggs] < floors:
        moves += 1
        for egg in range(eggs, 0, -1):
            reachable[egg] += reachable[egg - 1] + 1

    return moves


assert minimum_egg_drops(1, 5) == 5
assert minimum_egg_drops(2, 10) == 4
assert minimum_egg_drops(3, 14) == 4
