citylist = [
    (0, "Oradea"),
    (1, "Zerind"),
    (2, "Arad"),
    (3, "Timisoara"),
    (4, "Lugoj"),
    (5, "Mehadia"),
    (6, "Drobeta"),
    (7, "Sibiu"),
    (8, "Craiova"),
    (9, "Rimnicu Vilcea"),
    (10, "Fagaras"),
    (11, "Pitesti"),
    (12, "Neamt"),
    (13, "Bucharest"),
    (14, "Giurgiu"),
    (15, "Urziceni"),
    (16, "Iasi"),
    (17, "Vaslui"),
    (18, "Hirsova"),
    (19, "Eforie"),
]

weightmap = [
    #0   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15  16  17  18  19
    [0,  71, 0,  0,  0,  0,  0,  151,0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],# 0
    [71, 0,  75, 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],# 1
    [0,  75, 0,  118,0,  0,  0,  140,0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],# 2
    [0,  0,  118,0,  111,0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],# 3
    [0,  0,  0,  111,0,  70, 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],# 4
    [0,  0,  0,  0,  70, 0,  75, 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],# 5
    [0,  0,  0,  0,  0,  75, 0,  0,  120,0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],# 6
    [151,0,  140,0,  0,  0,  0,  0,  0,  80, 99, 0,  0,  0,  0,  0,  0,  0,  0,  0],# 7
    [0,  0,  0,  0,  0,  0,  120,0,  0,  146,0,  138,0,  0,  0,  0,  0,  0,  0,  0],# 8
    [0,  0,  0,  0,  0,  0,  0,  80, 146,0,  0,  97, 0,  0,  0,  0,  0,  0,  0,  0],# 9
    [0,  0,  0,  0,  0,  0,  0,  99, 0,  0,  0,  0,  0,  211,0,  0,  0,  0,  0,  0],# 10
    [0,  0,  0,  0,  0,  0,  0,  0,  138,97, 0,  0,  0,  101,0,  0,  0,  0,  0,  0],# 11
    [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  87, 0,  0,  0],# 12
    [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  211,101,0,  0,  90, 85, 0,  0,  0,  0],# 13
    [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  90, 0,  0,  0,  0,  0,  0],# 14
    [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  85, 0,  0,  0,  142,98, 0],# 15
    [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  87, 0,  0,  0,  0,  92, 0,  0],# 16
    [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  142,92, 0,  0,  0],# 17
    [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  98, 0,  0,  0,  86],#18
    [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  86, 0],# 19
]

positions = {
    0:  (250,160),   #Oradea
    1:  (190,265),   #Zerind
    2:  (145,370),   #Arad
    3:  (155,575),   #Timisoara
    4:  (340,660),   #Lugoj
    5:  (345,750),   #Mehadia
    6:  (335,850),   #Drobeta
    7:  (445,450),   #Sibiu
    8:  (660,885),   #Craiova
    9:  (510,575),   #Rimnicu Vilcea
    10: (700,475),   #Fagaras
    11: (735,580),   #Pitesti
    12: (955,250),   #Neamt
    13: (990,785),   #Bucharest
    14: (870,925),   #Giurgiu
    15: (1085,725),  #Urziceni
    16: (1125,330),  #Iasi
    17: (1220,485),  #Vaslui
    18: (1280,725),  #Hirsova
    19: (1355,870)   #Eforie
}

from collections import deque
import tkinter as tk

def verifyWeightmap():
    graphGood = True
    x = len(weightmap)
    y = len(weightmap[1])
    if x != y: 
        graphGood = False
    print(f"{x} x {y} grid is {"good"if x==y else "bad"}. Checking Symmetry")
    symmetryGood = True
    for i in range(x):
        for j in range(y):
            if weightmap[i][j] != weightmap[j][i]:
                print(f"Fail on {i}, {j}")
                symmetryGood = False
    print(f"Symmetry {"good" if symmetryGood else "bad"}.")
    return graphGood & symmetryGood
        
def getIndex() -> int:
    cityName = input("Input the name of city: ")
    if cityName.isdigit() :
        if (int(cityName) < len(citylist)):
            return int(cityName)
    return getIndexFromName(cityName)

def getNeighbors(node):
    neighbors = []
    if node < len(weightmap):
        for i in range(len(weightmap[node])):
            if weightmap[node][i] != 0:
                neighbors.append(i)
    return neighbors
    
        

def getIndexFromName(cityName):
    #Get the index of the name of a city
    for i, name in citylist:
        if name == cityName:
            return i
    return None

def getShortestPath(source, dest):
    neighbors = deque([int(source)])
    visited = []
    sz = len(weightmap[0])
    weightlist = [0]*sz
    parentlist = [None]*sz

    while neighbors:
        node = neighbors.popleft()
        if node not in visited:
                visited.append(node)
                nb = getNeighbors(node)
                for n in nb:
                    if weightmap[node][n] + weightlist[node] < weightlist[n] or weightlist[n] == 0:
                        weightlist[n] = weightmap[node][n] + weightlist[node]
                        parentlist[n] = node
                    if n not in visited and n not in neighbors:
                        neighbors.append(n)

    print(f"\nShortest path from {citylist[source][1]} to {citylist[dest][1]} is {weightlist[dest]}km:")
    t = dest
    path = deque()
    c=0
    while t != source:
        path.appendleft(t)
        t = parentlist[t]
        c+=1 
        if c > 1000:
            print("Error: Timeout")
            break
    print(citylist[source][1],end="")
    for city in path:
        print(f" -> {citylist[city][1]}", end="")
    path.appendleft(source)
    return path, weightlist[dest]

selected_cities = []
node_ids = []
line_ids = []

def oncityclick(event):
    for idx, (x,y) in positions.items():
        cx, cy = canvas.coords(f"node{idx}")[:2]
        cx += noderad
        cy += noderad
        if abs(event.x -cx) < noderad and abs(event.y - cy) < noderad:
            if len(selected_cities) == 2:
                selected_cities.clear()
            selected_cities.append(idx)
            update(canvas)
    

#_________MAIN________

noderad = 15
linewidth = 3
line_col = "gray"
node_col = "lightblue"
backg_col = "white"
selectedline_col = "pink"
highlighted_col = "red"

# Calculate bounding box and aspect ratio
xs = [x for x, y in positions.values()]
ys = [y for x, y in positions.values()]
min_x, max_x = min(xs), max(xs)
min_y, max_y = min(ys), max(ys)
margin = 50
data_width = max_x - min_x
data_height = max_y - min_y
aspect_ratio = data_width / data_height if data_height != 0 else 1

canvas_width = data_width + 2 * margin
canvas_height = data_height + 2 * margin

root = tk.Tk()
root.title("Prac 1 Vaughan Todd 22139124")
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg=backg_col)
canvas.pack(fill=tk.BOTH, expand=True)

def redraw(canvas, width, height):
    # Lock aspect ratio
    if width / height > aspect_ratio:
        # Too wide, adjust width
        width = int(height * aspect_ratio)
    else:
        # Too tall, adjust height
        height = int(width / aspect_ratio)
    canvas.config(width=width, height=height)
    canvas.delete("all")
    scale = min((width - 2 * margin) / data_width, (height - 2 * margin) / data_height)

    def get_scaled_pos(x, y):
        sx = (x - min_x) * scale + margin
        sy = (y - min_y) * scale + margin
        return sx, sy

    # Draw edges
    for i in range(len(weightmap)):
        for j in range(len(weightmap[i])):
            if weightmap[i][j] != 0:
                x1, y1 = get_scaled_pos(*positions[i])
                x2, y2 = get_scaled_pos(*positions[j])
                canvas.create_line(x1, y1, x2, y2, fill=line_col, width=linewidth, tags = f"line{i}{j}")
    
    # Draw nodes
    for idx, (x, y) in positions.items():
        city_name = citylist[idx][1]
        cx, cy = get_scaled_pos(x, y)
        canvas.create_oval(cx-noderad, cy-noderad, cx+noderad, cy+noderad, fill=node_col, outline="", tags = f"node{idx}")
        canvas.create_text(cx, cy-25, text=city_name, font=("Arial", 10))

    canvas.create_text(width/3,height/10, text="Path Distance: ", font=("Arial", 20), tags = f"text", anchor = "w")

def update(canvas):

    path = []

    if len(selected_cities) == 2:
        path, length = getShortestPath(selected_cities[0], selected_cities[1])
        canvas.itemconfig(f"text", text = f"Path Distance: {length}km")
    else:
        canvas.itemconfig(f"text", text = f"Path Distance: ")
            

    for idx, name in citylist:
        if idx in selected_cities:
            canvas.itemconfig(f"node{idx}",fill = highlighted_col)
        elif idx in path:
            canvas.itemconfig(f"node{idx}",fill = selectedline_col)
        else:
            canvas.itemconfig(f"node{idx}", fill = node_col)
    
    for i in range(len(weightmap)):
        for j in range(len(weightmap[i])):
            canvas.itemconfig(f"line{i}{j}", fill = line_col)

    for line in range(1,len(path)):
        idx_0, idx_1 = path[line-1],path[line]
        canvas.itemconfig(f"line{idx_0}{idx_1}",fill=selectedline_col)
        canvas.itemconfig(f"line{idx_1}{idx_0}",fill=selectedline_col)


    
    


    

    

def on_canvas_resize(event):
    redraw(canvas, event.width, event.height)

canvas.bind("<Configure>", on_canvas_resize)
canvas.bind("<Button-1>", oncityclick)

root.mainloop()



"""

source = getIndex()
if source == None:
    print(f"{source} is not a city")   
dest = getIndex()
if dest == None:
    print(f"{source} is not a city")
getShortestPath(source,dest)

"""

