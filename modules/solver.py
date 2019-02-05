def permutations(values, row, n=0):
    if values and values[0]:
        current, *other = values
        for i in range(len(row)-sum(other)-len(other)+1-current):
            if 1 not in row[i:i+current]:
                for j in permutations(other, row[i+current+1:], 1):
                    yield [1]*(i+n) + [2]*current + j
    else:
        yield []

def solve_row(values, row):
    valid_permutations = []
    for permutation in permutations(values, row):
        permutation += [1]*(len(row)-len(permutation))
        for n1, n2 in zip(row, permutation):
            if n1>0 and n1 != n2:
                break
        else:
            valid_permutations.append(permutation)

    new_row = valid_permutations[0]
    for permutation in valid_permutations[1:]:
        new_row = [n if n==r else 0 for n, r in zip(new_row, permutation)]

    return new_row

def solve(row_values, col_values, grid):
    changed = True
    while changed:
        changed = False
        for y, row_value in enumerate(row_values):
            row = solve_row(row_value, grid[y])
            for x, cell in enumerate(row):
                if cell and grid[y][x] != cell:
                    changed = True
                grid[y][x] = cell

        for x, col_value in enumerate(col_values):
            col = solve_row(col_value, [row[x] for row in grid])
            for y, cell in enumerate(col):
                if cell and grid[y][x] != cell:
                    changed = True
                grid[y][x] = cell

def main(inputs):
    width, height, columns, rows = inputs.split("\n")
    width, height = int(width), int(height)
    columns = [[int(n) for n in line.split(",")] for line in columns[1:-1].split('","')]
    rows = [[int(n) for n in line.split(",")] for line in rows[1:-1].split('","')]

    grid = [[0]*width for i in range(height)]

    solve(rows, columns, grid)

    return "\n".join([*("".join(["- *"[item] for item in row]) for row in grid), ""])

print(main('''5
5
"5","2,2","1,1","2,2","5"
"5","2,2","1,1","2,2","5"'''))

print(main('''8
11
"0","9","9","2,2","2,2","4","4","0"
"0","4","6","2,2","2,2","6","4","2","2","2","0"'''))

print(main('''30
20
"1","1","2","4","7","9","2,8","1,8","8","1,9","2,7","3,4","6,4","8,5","1,11","1,7","8","1,4,8","6,8","4,7","2,4","1,4","5","1,4","1,5","7","5","3","1","1"
"8,7,5,7","5,4,3,3","3,3,2,3","4,3,2,2","3,3,2,2","3,4,2,2","4,5,2","3,5,1","4,3,2","3,4,2","4,4,2","3,6,2","3,2,3,1","4,3,4,2","3,2,3,2","6,5","4,5","3,3","3,3","1,1"'''))

print(main('''30
30
"9,9","10,9","10,5,3","10,3,1","10,2,3","11,3","13,6","15,7","15,7","14,7","14,7","14,2,4","14,1,4","14,2,3","13,3,1","13,3","13,4","9,6,1","9,6,2","8,1,1,1,2,1","7,6,1","7,6","7,8","6,9","2,1,9","1,9","1,8","1,8","1,7","1,4,6"
"30","25","24,1","24,1","25,1","24,1","23","20,3,2","19,8","16,8","12,8","11,10","11,11","7,10","2,9","1,7","1,2,2","3","3","6","7","4,7","5","5,4","3,5","3,5","2,8","3,11","3,10,1","13,4"'''))