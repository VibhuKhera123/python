def dfs(maze, start, end):
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    stack = [start]
    visited = set()
    visited.add(start)
    path = {}

    while stack:
        current = stack.pop()
        if current == end:
            break
        for direction in directions:
            x, y = current
            dx, dy = direction
            next_pos = (x + dx, y + dy)
            if 0 <= next_pos[0] < len(maze) and 0 <= next_pos[1] < len(maze[0]) and maze[next_pos[0]][next_pos[1]] == 0 and next_pos not in visited:
                stack.append(next_pos)
                visited.add(next_pos)
                path[next_pos] = current

    if end not in visited:
        return None

    # Reconstruct the path
    shortest_path = []
    current = end
    while current != start:
        shortest_path.append(current)
        current = path[current]
    shortest_path.append(start)
    shortest_path.reverse()

    return shortest_path

# Get user input for maze dimensions
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

# Get user input for the maze
print("Enter the maze (0 for path, 1 for wall):")
maze = []
for _ in range(rows):
    row = list(map(int, input().split()))
    maze.append(row)

# Get user input for start and end points
start = tuple(map(int, input("Enter the start point (row col): ").split()))
end = tuple(map(int, input("Enter the end point (row col): ").split()))

# Print the maze
print("\nMaze:")
for row in maze:
    print(" ".join(map(str, row)))

# Find the shortest path using DFS
shortest_path = dfs(maze, start, end)

# Print the result
if shortest_path:
    print("\nShortest path found:")
    for row_idx in range(rows):
        for col_idx in range(cols):
            if (row_idx, col_idx) == start:
                print("S", end=" ")
            elif (row_idx, col_idx) == end:
                print("E", end=" ")
            elif (row_idx, col_idx) in shortest_path:
                print("P", end=" ")
            elif maze[row_idx][col_idx] == 1:
                print("#", end=" ")
            else:
                print("-", end=" ")
        print()
else:
    print("\nNo path found")
