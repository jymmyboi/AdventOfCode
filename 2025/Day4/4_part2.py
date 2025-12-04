with open("2025/Day4/4.txt") as file:
    raw_lines = file.readlines()
    lines = [line.strip() for line in raw_lines]

def create_grid(lines):
    grid = {}

    for x, row in enumerate(lines):
        for y, cell in enumerate(row):
            grid[(x,y)] = cell
    return grid

def check_directions(grid):
    to_clear = []
    paper_total = 0
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
    for i in grid:
        roll_count = 0
        sx, sy = i
        if grid.get(i) == '@':
            for direction in directions:
                chk_x = sx + directions[direction][0]
                chk_y = sy + directions[direction][1]
                if not (chk_x, chk_y) in grid.keys():
                    continue
                if grid.get((chk_x,chk_y)) == '@':
                    roll_count += 1
            if roll_count < 4:
                paper_total += 1
                to_clear.append(i)

    print(f"run total: {paper_total}")
    for cell in to_clear:
        grid[cell] = "."
    return paper_total



grid = create_grid(lines)

paper_total = 0

complete = False
while not complete:
    run = check_directions(grid)
    if run == 0:
        complete = True
    else:
        paper_total += run

print(paper_total)


