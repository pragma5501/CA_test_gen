import random
import sys


if len(sys.argv) < 3:
    sys.exit()


test_type = int(sys.argv[1])
random.seed(int(sys.argv[2]))

def generate_test_case1(n_max=99999):
    n = random.randint(1, n_max)
    print(n)

def generate_test_case2(n_max=100000):
    n = random.randint(1, n_max)
    print(n)
    
def generate_test_case3(n_max=1000, w_max=100):
    n = random.randint(2, n_max)
    e = random.randint(0, n * (n - 1) // 2)
    k = random.randint(0, max(0, n - 2))

    edges = set()
    while len(edges) < e:
        a = random.randint(1, n)
        b = random.randint(1, n)
        if a != b:
            a, b = sorted([a, b])
            edges.add((a, b, random.randint(1, w_max)))

    patrol_nodes = set()
    while len(patrol_nodes) < k:
        p = random.randint(2, n-1)
        patrol_nodes.add(p)

    print(f"{n} {e} {k}")
    for edge in edges:
        print(f"{edge[0]} {edge[1]} {edge[2]}")
    for p in patrol_nodes:
        print(p)

def generate_test_case4(n_max=100000):
    n = random.randint(1, n_max) 


    animals = [0] * n  
    animals[0] = 0 
    tiger_index = random.randint(1, n-1)  
    animals[tiger_index] = 2  
    for i in range(1, n):
        if i != tiger_index:
            animals[i] = random.randint(0, 1)  

   
    edges = []
    children_counts = [0] * (n + 1) 
    for i in range(2, n + 1):
        parent = random.randint(1, i - 1)
        
        while children_counts[parent] == 2:
            parent = random.randint(1, i - 1)
        edges.append((parent, i))
        children_counts[parent] += 1

    
    print(n)
    print(" ".join(map(str, animals)))
    for edge in edges:
        print(f"{edge[0]} {edge[1]}")
def generate_test_case5():
    # Generate number of pens (N) and number of possible connections (M)
    N = random.randint(1, 100)
    M = random.randint(1, N * (N - 1) // 2)

    # Generate M connections with time T to move sheep between pens A and B
    connections = set()
    while len(connections) < M:
        A = random.randint(1, N)
        B = random.randint(1, N)
        while A == B:
            B = random.randint(1, N)
        # Ensure A and B are in sorted order to prevent duplicates like (1, 2) and (2, 1)
        A, B = sorted((A, B))
        T = random.randint(1, 100)
        connections.add((A, B, T))

    # Generate number of infected pens (K) and their numbers
    K = random.randint(0, N % 5)
    infected_pens = random.sample(range(1, N + 1), K)

    # Generate the number of the safe pen
    safe_pen = random.randint(1, N)

    # Print the test case
    print(f"{N} {M}")
    for connection in connections:
        print(f"{connection[0]} {connection[1]} {connection[2]}")
    print(K)
    print(" ".join(map(str, infected_pens)))
    print(safe_pen)

if test_type == 1:
    generate_test_case1()
if test_type == 2:
    generate_test_case2()
if test_type == 3:
    generate_test_case3()
if test_type == 4:
    generate_test_case4()
    
if test_type == 5:
    generate_test_case5()
