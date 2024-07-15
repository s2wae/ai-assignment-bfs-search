import math
import tkinter as tk
import collections

# Define drawing functions for hexagons, legends, traps, and rewards
def draw_hexagon(canvas, x, y, coord):
    size = 30
    points = []
    for i in range(6):
        angle_deg = 60 * i
        angle_rad = math.radians(angle_deg)
        point_x = x + size * math.cos(angle_rad)
        point_y = y + size * math.sin(angle_rad)
        points.append((point_x, point_y))

    canvas.create_polygon(points, outline="black", fill="#F9D89B")
    canvas.create_text(x, y, text=coord, fill="black")

def draw_legend(canvas, x, y, color):
    size = 20
    points = []
    for i in range(6):
        angle_deg = 60 * i
        angle_rad = math.radians(angle_deg)
        point_x = x + size * math.cos(angle_rad)
        point_y = y + size * math.sin(angle_rad)
        points.append((point_x, point_y))

    return canvas.create_polygon(points, outline="black", fill=color)

def draw_TrapText(canvas, x, y, text):
    canvas.create_text(x, y, text=text, font=("Arial", 5, "bold"), fill="black")

def draw_RewardText(canvas, x, y, text):
    canvas.create_text(x, y, text=text, font=("Arial", 4, "bold"), fill="black")

# Create tkinter window and canvas
window = tk.Tk()
window.title("Breadth First Search Algorithm")
canvas = tk.Canvas(window, width=500, height=400, background="#AAE8AA")
canvas.pack()

# Define custom coordinates for hexagons
custom_coords = [
    [(1, 1), (2, 3), (3, 4), (4, 6), (5, 7), (6, 9)],
    [(2, 1), (2, 2), (3, 3), (4, 5), (5, 6), (6, 8)],
    [(3, 1), (3, 2), (4, 4), (5, 5), (6, 7), (7, 8)],
    [(4, 1), (4, 2), (4, 3), (5, 4), (6, 6), (7, 7)],
    [(5, 1), (5, 2), (5, 3), (6, 5), (7, 6), (8, 8)],
    [(6, 1), (6, 2), (6, 3), (6, 4), (7, 5), (8, 7)],
    [(7, 1), (7, 2), (7, 3), (7, 4), (8, 6), (9, 7)],
    [(8, 1), (8, 2), (8, 3), (8, 4), (8, 5), (9, 6)],
    [(9, 1), (9, 2), (9, 3), (9, 4), (9, 5), (10, 7)],
    [(10, 1), (10, 2), (10, 3), (10, 4), (10, 5), (10, 6)]
]

# Function to draw the hexagon map
def printMap():
    for i in range(len(custom_coords)):
        for j in range(len(custom_coords[i])):
            coord = f"{custom_coords[i][j][0]},{custom_coords[i][j][1]}"
            if i % 2 == 0:
                x = 50 + (90 * (i // 2))
                y = 75 + (50 * j)
            else:
                x = 95 + (90 * (i // 2))
                y = 50 + (50 * j)
            draw_hexagon(canvas, x, y, coord)

printMap()

# BFS algorithm to find the path
def bfs(start_node, graph):
    visited = set()
    queue = collections.deque([start_node])
    path = []

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            path.append(node)
            if node in graph:
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        queue.append(neighbor)

    return path

# Define the graph structure
graph = {
    '1,1': ['2,1', '2,3'],
    '2,1': ['3,1'],
    '2,2': [],
    '2,3': ['3,3', '3,4'],
    '3,1': ['4,1', '3,2'],
    '3,2': ['4,3'],
    '3,3': ['4,5'],
    '3,4': [],
    '4,1': ['5,1'],
    '4,2': [],
    '4,3': ['5,2'],
    '4,4': [],
    '4,5': ['5,5', '5,6'],
    '4,6': [],
    '5,1': ['6,1', '6,2'],
    '5,2': ['6,3'],
    '5,3': [],
    '5,4': [],
    '5,5': ['6,6'],
    '5,6': ['5,7', '6,8'],
    '5,7': ['6,9'],
    '6,1': ['7,1'],
    '6,2': [],
    '6,3': ['7,3'],
    '6,4': [],
    '6,5': ['7,5'],
    '6,6': ['6,5', '7,7'],
    '6,7': [],
    '6,8': ['6,9', '7,8'],
    '6,9': [],
    '7,1': ['8,1', '8,2'],
    '7,2': [],
    '7,3': ['8,3', '8,4'],
    '7,4': [],
    '7,5': ['8,7'],
    '7,6': [],
    '7,7': ['8,8'],
    '7,8': [],
    '8,1': ['9,1'],
    '8,2': [],
    '8,3': [],
    '8,4': ['9,4'],
    '8,5': [],
    '8,6': [],
    '8,7': ['9,7'],
    '8,8': [],
    '9,1': ['10,1', '10,2'],
    '9,2': [],
    '9,3': [],
    '9,4': ['10,4'],
    '9,6': [],
    '9,7': [],
    '10,1': [],
    '10,2': [],
    '10,3': [],
    '10,4': []
}

# Function to animate the path on the canvas
def animate_path(canvas, path):
    delay = 1000  # Delay between steps in milliseconds
    for step, node in enumerate(path):
        x, y = get_coordinates(node)
        canvas.after(delay * step, highlight_hexagon, canvas, x, y, node, path)

def highlight_hexagon(canvas, x, y, node, path):
    size = 30
    points = []
    for i in range(6):
        angle_deg = 60 * i
        angle_rad = math.radians(angle_deg)
        point_x = x + size * math.cos(angle_rad)
        point_y = y + size * math.sin(angle_rad)
        points.append((point_x, point_y))

    canvas.create_polygon(points, outline="black", fill="yellow", tags="highlight")
    canvas.update()
    canvas.after(500)  # Keep highlighted for 500 milliseconds
    canvas.delete("highlight")  # Remove highlight

    # Print current position
    print(f"Current position: ({node})")

    # If it's the last node in the path, print the solution path
    if node == path[-1]:
        print(f"Solution path: ({path})")

# Function to get coordinates based on custom_coords structure
def get_coordinates(node):
    for i in range(len(custom_coords)):
        for j in range(len(custom_coords[i])):
            coord = f"{custom_coords[i][j][0]},{custom_coords[i][j][1]}"
            if coord == node:
                if i % 2 == 0:
                    x = 50 + (90 * (i // 2))
                    y = 75 + (50 * j)
                else:
                    x = 95 + (90 * (i // 2))
                    y = 50 + (50 * j)
                return x, y

# Draw legends, traps, and rewards on the canvas
treasure1 = draw_legend(canvas, 185, 250, "orange")
treasure2 = draw_legend(canvas, 230, 125, "orange")
treasure3 = draw_legend(canvas, 365, 200, "orange")
treasure4 = draw_legend(canvas, 455, 200, "orange")

obstacle1 = draw_legend(canvas, 50, 225, "grey")
obstacle2 = draw_legend(canvas, 140, 175, "grey")
obstacle3 = draw_legend(canvas, 185, 200, "grey")
obstacle4 = draw_legend(canvas, 230, 175, "grey")
obstacle5 = draw_legend(canvas, 230, 275, "grey")
obstacle6 = draw_legend(canvas, 320, 225, "grey")
obstacle7 = draw_legend(canvas, 320, 275, "grey")
obstacle8 = draw_legend(canvas, 365, 250, "grey")
obstacle9 = draw_legend(canvas, 410, 125, "grey")

trap1 = draw_legend(canvas, 410, 175, "#F99DF9")
draw_TrapText(canvas, 410, 175, "Trap 1")
trap2 = draw_legend(canvas, 95, 100, "#F99DF9")
draw_TrapText(canvas, 95, 100, "Trap 2")
trap3 = draw_legend(canvas, 140, 275, "#F99DF9")
draw_TrapText(canvas, 140, 275, "Trap 2")
trap4 = draw_legend(canvas, 275, 200, "#F99DF9")
draw_TrapText(canvas, 275, 200, "Trap 3")
trap5 = draw_legend(canvas, 320, 125, "#F99DF9")
draw_TrapText(canvas, 320, 125, "Trap 3")
trap6 = draw_legend(canvas, 185, 100, "#F99DF9")
draw_TrapText(canvas, 185, 100, "Trap 4")

reward1 = draw_legend(canvas, 95, 200, "#4EEB4E")
draw_RewardText(canvas, 95, 200, "Reward 1")
reward2 = draw_legend(canvas, 230, 75, "#4EEB4E")
draw_RewardText(canvas, 230, 75, "Reward 1")
reward3 = draw_legend(canvas, 275, 300, "#4EEB4E")
draw_RewardText(canvas, 275, 300, "Reward 2")
reward4 = draw_legend(canvas, 365, 150, "#4EEB4E")
draw_RewardText(canvas, 365, 150, "Reward 2")

# Execute BFS algorithm and get the path
start_node = '1,1'
path = bfs(start_node, graph)

# Execute animation of the path
animate_path(canvas, path)

# Start tkinter main loop
window.mainloop()