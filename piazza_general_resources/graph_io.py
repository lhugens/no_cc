import networkx
import time
import random
import gzip
import sys
from connected_components import connected_components
from my_connected_components import my_no_connected_components

def mk_instance(n, k, r):
    """Set random seed to 'r' and create a graph with 'n' vertices and (up to) n * k edges."""
    random.seed(r)
    V = list(range(1,n+1))
    E = set()
    for _ in range(n*k):
        i = random.randint(1,n)
        j = random.randint(1,n)
        if i != j:
            i, j = min(i,j), max(i,j)
            E.add((i,j))
    return V, E


def write_instance(V, E, filename):
    """Write a graph instance to a file (loosely, in a format used in DIMACS challenges)."""
    with open(filename, "w") as f:
        f.write(f"Nodes {n}\n")
        f.write(f"Edges {len(E)}\n")
        for (i,j) in E:
            f.write(f"E {i} {j}\n")


def read_instance(filename):
    """Read a graph from a file."""
    try:
        if len(filename)>3 and filename[-3:] == ".gz":  # file compressed with gzip
            import gzip
            f = gzip.open(filename, "rt")
        else:   # usual, uncompressed file
            f = open(filename)
    except IOError:
        print("could not open file", filename)
        exit(-1)

    edges = set()
    for line in f:
        if line[0:6].lower() == 'edges ':
            e, n_edges = line.split()
            n_edges = int(n_edges)
        elif line[0:6].lower() == 'nodes ':
            e, n_nodes = line.split()
            n_nodes = int(n_nodes)
        elif line[0:2].lower() == 'e ':
            e, i, j = line.split()
            i, j = int(i), int(j)
            i, j = min(i,j), max(i,j)
            edges.add((i,j))
    f.close()

    assert n_edges == len(edges)
    vertices = list(range(1,n_nodes+1))
    return vertices, list(edges)


if __name__ == "__main__":
    for n in [100, 1000, 10000, 100000, 1000000]:
        for k in [1, 2, 5, 10]:
            for r in range(1,11):
                
                # # uncomment for creating files with graphs (may be rather large):
                # V, E = mk_instance(n, k, r)
                # filename = f"G{n}-{k}-{r}.graph"
                # write_instance(V, E, filename)
                # print(n, k, len(E), connected_components(V, E))
                #  
                # # uncomment for reading graphs from files and solving with 'default' and the alternative method:
                filename = f"G{n}-{k}-{r}.graph"
                V, E = read_instance(filename)

                start = time.process_time()
                ncomponents = connected_components(V,E)
                end = time.process_time()
                cpu_default = end - start
                print(f"{filename}: {ncomponents} components, {cpu_default} seconds")
                start = time.process_time()
                ncomponents = my_no_connected_components(V,E)
                end = time.process_time()
                cpu_alternative = end - start
                print(f"{filename}: {ncomponents} components, {cpu_alternative} seconds")
                print("cpu seconds ration", cpu_alternative / cpu_default) 
                print()
                
                # # uncomment for creating benchmark set in memory and solving with 'default' method:
                # V, E = mk_instance(n, k, r)
                # start = time.process_time()
                # ncomponents = connected_components(V,E)
                # end = time.process_time()
                # cpu = end - start
                # print(f"{filename}: {ncomponents} components, {cpu} seconds")
                
    # # uncomment for reading a graphs from a particular file and solving with 'default' method
    # if len(sys.argv) != 2:
    #     print(f"usage: {sys.argv[0]} filename\nwhere filename is the instance to be solved")
    # filename = sys.argv[1]
    # V, E = read_instance(filename)
    # start = time.process_time()
    # ncomponents = connected_components(V,E)
    # end = time.process_time()
    # cpu = end - start
    # print(f"{filename}: {ncomponents} components, {cpu} seconds")
