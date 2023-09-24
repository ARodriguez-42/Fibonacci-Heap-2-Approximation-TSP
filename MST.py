import numpy as np
from fib import FibHeap

# Read the file containing the tree information 
def adjList(name):
    f = open(name,"r")
    lines = f.readlines()
    n = int(lines[0])
    m = int(lines[1])
    matrix = np.zeros(shape=(m,3), dtype=int)
    for a in range(2,2+m):
        line = lines[a].split()
        matrix[a - 2][0] = int(line[0])
        matrix[a - 2][1] = int(line[1])
        matrix[a - 2][2] = int(line[2])
    matrix = matrix[matrix[:,2].argsort()]
    #print(type(matrix[0][0]))
    return matrix, n, m

# MST Solver
def MSTsolver(fib:FibHeap, n:int):
    #the visited array will be used to track whether the node has been visited
    visitied = [False for x in range(n)]
    #visitiedCount will be used to stop the while loop
    visitiedCount = 0
    #MSTweight will be used to keep track of the total weight
    MSTweight = 0
    #minSpanTree will be used to stored the edge pairs used in the MST
    minSpanTree = list()
    while visitiedCount < n:
        #retrieve the min node in the heap and store the FibNode
        shortest = fib.min
        vert = shortest.vertices
        v1 = vert[0]
        v2 = vert[1]
        dist = shortest.val
        if visitied[v1] == False or visitied[v2] == False:
            if visitied[v1] == False:
                visitied[v1] = True
                visitiedCount +=1
            if visitied[v2] == False:
                visitied[v2] = True
                visitiedCount += 1
            minSpanTree.append(shortest.vertices)
            MSTweight += dist
            fib.delete_min()
        else:
            fib.delete_min()
    return minSpanTree, MSTweight
        
def find_mst(adj_list, num_vertices):
    visited = [False] * num_vertices
    mst = []

    # Start with the first vertex
    visited[0] = True

    while len(mst) < num_vertices - 1:
        min_weight = float('inf')
        min_edge = None

        # Find the minimum weight edge from the visited vertices
        for edge in adj_list:
            u, v, weight = edge
            if visited[u] and not visited[v] and weight < min_weight:
                min_weight = weight
                min_edge = edge

        if min_edge is not None:
            u, v, weight = min_edge
            mst.append(min_edge)
            visited[v] = True

    return mst

#Computes TSP journey based on the Walk given
def tsp_journey(adj_list, cycle):
    weight = 0
    for i in range(len(cycle)-1):
        for edge in adj_list:
            if (edge[0] == cycle[i] or edge[0] == cycle[i+1]):
                if(edge[1] == cycle[i] or edge[1] == cycle[i+1]):
                    weight += edge[2]
                    break
    return weight

def tsp_approximation(adj_list, mst, num_vertices):

    # Perform DFS traversal on the MST to obtain a tour
    visited = [False] * num_vertices
    tour = []

    def dfs(vertex):
        visited[vertex] = True
        tour.append(vertex)

        for edge in mst:
            u, v = edge
            if u == vertex and not visited[v]:
                dfs(v)

    dfs(0)

    #print(tour)
    # Remove duplicate vertices to obtain a Hamiltonian cycle
    hamiltonian_cycle = list(dict.fromkeys(tour))
    #print(hamiltonian_cycle)
    hamiltonian_cycle.append(0)

    # Calculate the total weight of the Hamiltonian cycle and its journey
    tsp_cost = tsp_journey(adj_list, hamiltonian_cycle)
    hamiltonian_cycle.pop()
    return hamiltonian_cycle, tsp_cost


if __name__ == '__main__':

    # User will input file name in terminal
    #fileName = input("Enter file name: ")

    fileName = "test.txt"
    aList, n, m = adjList(fileName)

    # Creating the FibHeab
    fib = FibHeap()

    # Will populate the FibHeab with the adjacency list created from the file
    for path in aList:
        v1 = path[0]
        v2 = path[1]
        vertices = (v1, v2)
        dist = path[2]
        fib.insert(dist, vertices)
    

    tree, total = MSTsolver(fib, n)
    print("Edges:", tree)
    print("Total Edge Weight: ", total)

    # MST to TSP

    tsp_solution, tsp_weight = tsp_approximation(aList, tree, n)

    print("TSP Tour:", tsp_solution)
    print("TSP weight:", tsp_weight)



    

