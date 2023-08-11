from queue import PriorityQueue

class Graph:
    def __init__(self,n):
        self.n = n
        self.edg = [[-1 for i in range(n)] for j in range(n)]
        self.vis = []
    
    def add_edg(self,u,v):
        self.edg[u][v] = 1

def pos_to_idx(i,j):
    global lines
    return i*len(lines[0])+j

def dijkstra(graph):
    global si,sj,ei,ej
    dis = {}
    for i in range(graph.n):
        dis[i] = 1e18

    dis[pos_to_idx(si,sj)] = 0

    pq = PriorityQueue()
    pq.put((0,pos_to_idx(si,sj)))

    while not pq.empty():
        (d,u) = pq.get()
        graph.vis.append(u)

        for v in range(graph.n):
            if graph.edg[u][v] != -1:
                if v not in graph.vis:
                    old_cost = dis[v]
                    new_cost = dis[u] + graph.edg[u][v]
                    if new_cost < old_cost:
                        pq.put((new_cost,v))
                        dis[v] = new_cost
    
    return dis[pos_to_idx(ei,ej)]

lines = open('inpd12.txt','r').read().split('\n')
si,sj,ei,ej = -1,-1,-1,-1

graph = Graph(len(lines)*len(lines[0]))

for i in range(len(lines)):
    for j in range(len(lines[0])):
        if lines[i][j] == 'S':
            si,sj = i,j
            lines[i] = lines[i].replace('S','a')
        elif lines[i][j] == 'E':
            ei,ej = i,j
            lines[i] = lines[i].replace('E','z')
for i in range(len(lines)):
    for j in range(len(lines[0])):        
        for i_ in range(-1,2):
            for j_ in range(-1,2):
                if (i_+j_) not in [-1,1] or (i+i_ < 0 or i+i_ >= len(lines)) or (j+j_ < 0 or j+j_ >= len(lines[0])):
                    continue
                if (ord(lines[i+i_][j+j_])-ord(lines[i][j])) <= 1:
                    graph.add_edg(pos_to_idx(i,j),pos_to_idx(i+i_,j+j_))

print(dijkstra(graph))