"""
Maze Generator and Solver (DFS)

Generates random maze with walls and solves using DFS.

"""

import random

def generate_maze(width=10, height=10):
    maze = [['#'] * width for _ in range(height)]
    def carve(x, y):
        maze[y][x] = ' '
        directions = [(2,0), (-2,0), (0,2), (0,-2)]
        random.shuffle(directions)
        for dx, dy in directions:
            nx, ny = x+dx, y+dy
            if 0 <= nx < width and 0 <= ny < height and maze[ny][nx] == '#':
                maze[ny - dy//2][nx - dx//2] = ' '
                carve(nx, ny)
    carve(1,1)
    maze[0][1] = 'S'  # Start
    maze[height-1][width-2] = 'E'  # End
    return maze

def print_maze(maze):
    for row in maze:
        print(''.join(row))

def solve_maze(maze):
    height = len(maze)
    width = len(maze[0])
    start = (0,1)
    end = (height-1,width-2)
    stack = [start]
    visited = set()
    parent = {}

    while stack:
        x,y = stack.pop()
        if (x,y) == end:
            break
        for nx, ny in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
            if 0 <= nx < height and 0 <= ny < width and maze[nx][ny] in (' ', 'E') and (nx,ny) not in visited:
                visited.add((nx,ny))
                parent[(nx,ny)] = (x,y)
                stack.append((nx,ny))
    else:
        print("No solution found.")
        return

    # Backtrack path
    path = []
    cur = end
    while cur != start:
        path.append(cur)
        cur = parent[cur]
    path.append(start)

    for (x,y) in path:
        if maze[x][y] == ' ':
            maze[x][y] = '.'

if __name__ == "__main__":
    maze = generate_maze()
    print("Generated Maze:")
    print_maze(maze)
    solve_maze(maze)
    print("\nSolved Maze:")
    print_maze(maze)
