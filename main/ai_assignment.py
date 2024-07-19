import math
import tkinter as tk

# this is the main bfs function that is used to find the solution path
def bfs(start_node, graph, visited):
    visited.append(start_node)
    queue = [start_node]
    temp_path = []

    while queue:
        n = queue.pop(0)
        temp_path.append(n)
        for neighbor in graph[n]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)

    return temp_path

# main function
def main(canvas):
    print("The resulting path with BFS to the treasures are:")

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

    start_node = '1,1'
    visited = []
    path = bfs(start_node, graph, visited)
    print(path)
    animate_path(canvas, path)

# opens a popup window to show the algorithm working on the map
window = tk.Tk()
window.title("Breadth First Search Algorithm")
canvas = tk.Canvas(window, width=500, height=400, background="#AAE8AA")
canvas.pack()

# this function  draws the hexagons on the map
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

# this draws the legend of the map
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

# this function and the draw_RewardText functions simply makes text for both trap and reward hexes
def draw_TrapText(canvas, x, y, text):
    canvas.create_text(x, y, text=text, font=("Arial", 5, "bold"), fill="black")


def draw_RewardText(canvas, x, y, text):
    canvas.create_text(x, y, text=text, font=("Arial", 4, "bold"), fill="black")


# this function is used to print the whole map for us to see
def printMap(canvas, custom_coords):
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


# this function calculates the energy for every step that we take on the map
def calculate_energy_step(path):
    energy = 0
    step = 0
    energy_increment = 1
    step_increment = 1

    energy_modifiers = {'4,5': 0.5, '5,1': 0.5}
    step_modifiers = {'8,3': 0.5, '8,7': 0.5}

    energy_history = []
    step_history = []

    for node in path:
        energy += energy_increment
        step += step_increment

        if node in energy_modifiers:
            energy_increment *= energy_modifiers[node]

        if node in step_modifiers:
            step_increment *= step_modifiers[node]

        energy_history.append(energy)
        step_history.append(step)

    return energy_history, step_history

# this plays through the solution path that we have gotten from using the bfs function, and it shows each step we take one by one
def animate_path(canvas, path):
    energy_history, step_history = calculate_energy_step(path)
    delay = 1000  # Delay between steps in milliseconds

    def after_animation_complete():
        final_energy = energy_history[-1]
        final_step = step_history[-1]
        print(f"Final energy: {final_energy}")
        print(f"Final step: {final_step}")

    def animate_step(step, node):
        x, y = get_coordinates(node)
        canvas.after(delay * step, highlight_hexagon, canvas, x, y, node, path, energy_history[step], step_history[step])
        if step == len(path) - 1:
            canvas.after(delay * (step + 1), after_animation_complete)

    for step, node in enumerate(path):
        animate_step(step, node)


# a function to highlight the current hex that the function is on
def highlight_hexagon(canvas, x, y, node, path, energy, step):
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
    canvas.after(500)
    canvas.delete("highlight")

    print(f"Current position: ({node}), Energy: {energy}, Step: {step}")

# this function gets the coordinates for each hex
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

# the hex coordinates
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

# the code below is to draw the whole map out
printMap(canvas, custom_coords)

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

main(canvas)

window.mainloop()