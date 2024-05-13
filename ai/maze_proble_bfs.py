# from collections import deque

# # Define the maze
# maze = [
#     [0, 1, 0, 0, 0],
#     [0, 1, 0, 1, 0],
#     [0, 0, 0, 0, 0],
#     [0, 1, 1, 1, 0],
#     [0, 0, 0, 1, 0]
# ]

# # Define the directions (up, down, left, right)
# directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

# def bfs(maze, start, end):
#     queue = deque([start])
#     visited = set()
#     visited.add(start)
#     path = {}

#     while queue:
#         current = queue.popleft()
#         if current == end:
#             break
#         for direction in directions:
#             x, y = current
#             dx, dy = direction
#             next_pos = (x + dx, y + dy)
#             if 0 <= next_pos[0] < len(maze) and 0 <= next_pos[1] < len(maze[0]) and maze[next_pos[0]][next_pos[1]] == 0 and next_pos not in visited:
#                 queue.append(next_pos)
#                 visited.add(next_pos)
#                 path[next_pos] = current

#     if end not in visited:
#         return None

#     # Reconstruct the path
#     shortest_path = []
#     current = end
#     while current != start:
#         shortest_path.append(current)
#         current = path[current]
#     shortest_path.append(start)
#     shortest_path.reverse()

#     return shortest_path

# # Define the start and end points
# start = (0, 0)
# end = (4, 4)

# # Find the shortest path using BFS
# shortest_path = bfs(maze, start, end)

# # Print the result
# if shortest_path:
#     print("Shortest path found:")
#     for row in range(len(maze)):
#         for col in range(len(maze[0])):
#             if (row, col) in shortest_path:
#                 print("P", end=" ")
#             else:
#                 print("-", end=" ")
#         print()
# else:
#     print("No path found")


from collections import deque

def bfs(maze, start, end):
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    queue = deque([start])
    visited = set()
    visited.add(start)
    path = {}

    while queue:
        current = queue.popleft()
        if current == end:
            break
        for direction in directions:
            x, y = current
            dx, dy = direction
            next_pos = (x + dx, y + dy)
            if 0 <= next_pos[0] < len(maze) and 0 <= next_pos[1] < len(maze[0]) and maze[next_pos[0]][next_pos[1]] == 0 and next_pos not in visited:
                queue.append(next_pos)
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

def print_maze(maze, path):
    for row in range(len(maze)):
        for col in range(len(maze[0])):
            if (row, col) == start:
                print("S", end=" ")
            elif (row, col) == end:
                print("E", end=" ")
            elif (row, col) in path:
                print("P", end=" ")
            else:
                print("-", end=" ")
        print()

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
print_maze(maze, set())

# Find the shortest path using BFS
shortest_path = bfs(maze, start, end)

# Print the result
if shortest_path:
    print("\nShortest path found:")
    print_maze(maze, set(shortest_path))
else:
    print("\nNo path found")
