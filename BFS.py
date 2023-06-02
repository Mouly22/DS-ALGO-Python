inp3 = open('/Users/mouly/Downloads/input2_3.txt', 'r')
class BFS_Travarsal:
    def __init__(self):
        self.graph = {}
        
    def bfs_construct(self, val1, val2):
        if val1 not in self.graph:
            self.graph[val1] = []
        if val2 not in self.graph:
            self.graph[val2] = []
        self.graph[val1].append(val2)
      
        
    def bfs_travs(self, start):
        lst = []
        lst.append(start)
        used = []
        while len(lst) != 0:
            v = lst.pop(0)
            #important part
            if v in self.graph.keys():
                if v not in used:
                    used.append(v)
                for elm in self.graph[v]:
                    lst.append(elm)
                    self.graph[v] = start
        print(used)

    
a = BFS_Travarsal()
line1 = inp3.readline().split()
for m in range(int(line1[1])):
    lines = inp3.readline().split()
    a.bfs_construct(int(lines[0]), int(lines[1]))
for m in a.graph.keys():
    a.bfs_travs(m)
    break