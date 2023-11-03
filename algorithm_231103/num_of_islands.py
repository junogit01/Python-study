gird = [
    ["1", "1", "1", "1", "0"]
    ["1", "1", "0", "0", "0"]
    ["0", "1", "0", "1", "0"]
    ["1", "0", "1", "0", "1"]
]

def num_islands(grid: list[list[str]]) -> int:
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if gird[i][j] == "1":
                stack = [(i, j)]
                while stack:
                    x, y = stack.pop()
                    east = (x + 1, y) # 1, 0
                    west = (x - 1, y) # -1, 0
                    south = (x, y + 1) # 0, 1
                    north = (x, y + 1) # 0, -1
                    direction = [east, west, south, north]
                    for x, y in direction:
                        if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
                            if grid[x][y] == "1":
                                grid[x][y] = "0"
                                stack.append((x, y))
                count += 1

    return count
print(num_islands(gird))