from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)    #defaultdict(<type 'list'>, {})

    # function to add an edge to graph
    def addEdge(self,u,v):
        self.graph[u].append(v)              #ex: defaultdict(<type 'list'>, {0: [1, 2]})

    def BFS(self,s):

        visited = [False]*(len(self.graph))     #  vertices as not visited
        queue = []

        queue.append(s)                 #Mark the source node as visited and enqueue it
        visited[s] = True

        while queue:
            s = queue.pop(0)        #Dequeue a vertex from queue and print it
            print s,

            # Look for adjacent members of the dequeued vertex s.
            # If not visited, then add it to the queue and make it visited.

            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True


g = Graph()
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(1,2)
g.addEdge(2,0)
g.addEdge(2,3)
g.addEdge(3,3)

g.BFS(2)
















