


def create_grid(rows):
    grid = {}

    for x, row in enumerate(rows):
        for y, cell in enumerate(row):
            grid[(x,y)] = cell
    return grid

def check_direction(start, direction, grid):

    sx, sy = start

    directions = {
        'nw': (-1, -1),
        'n': (0, -1),
        'ne': (1, -1),
        'e': (1, 0),
        'se': (1, 1),
        's': (0, 1),
        'sw': (-1, 1),
        'w': (-1, 0),
    }

    letters = ('M', 'A', 'S')

    for i in range(1, 4):
        new_index = (
            sx + directions[direction][0] * i,
            sy + directions[direction][1] * i,
        )
        if grid.get(new_index) != letters[i - 1]:
            return 0
    
    return 1

def check_for_xmas(index, grid):

    current = grid.get(index)
    if current != "X":
        return 0
    
    found = 0

    for direction in ["nw", "n", "ne", "e", "se", "s", "sw", "w"]:
        found += check_direction(index, direction, grid)
    
    return found

def part_1():
    with open("4.txt") as input:
        rows = input.readlines()
    
    grid = create_grid(rows)
    found = 0
    for index in grid:
        found += check_for_xmas(index, grid)
    # print(grid)
    print(f"Part 1: {found}")

part_1()

