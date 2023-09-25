#include <stdio.h>
#include <stdlib.h>  // Include the header for malloc

struct Tuple{
    int first;
    int second;
};

int dfs(int visited[], int V[], int lengthV, struct Tuple *E, int lengthE){
    int sum=0; 
    visited[0] = 1;
    for(int i=0; i<lengthV; i++){
        sum += V[i];
    }
    return sum;
}

int my_no_connected_components(int V[], int lengthV, struct Tuple* E, int lengthE){
    // create visited array
    int *visited = malloc(lengthV * sizeof(int)); // Allocate memory for the visited array
    if (visited == NULL) { // Handle memory allocation error if necessary
        return -1; // Indicate an error
    }
    for(int k=0; k<lengthV; k++){
        visited[k] = 0;
    }

    int ncc = 0;

    //for(int i=0; i<lengthE; i++){
    //    //if(visited[V[i]] == 0){
    //    //    dfs(V[i]);
    //    //}
    //    ncc += E[i].first;
    //}
    ncc = dfs(visited, V, lengthV, E, lengthE);
    return visited[0];
}

// class my_no_connected_components:
//     def __init__(self, g):
//         self.g = g
//         self.visited = {}
//         self.V = g.keys()
//         self.ncc = 0
//         for k in self.V:
//             self.visited[k] = self.visited.get(k, False)
// 
//     def find(self):
//         for k in self.V:
//             if self.visited[k] == False:
//                 self.dfs(k)
//                 self.ncc+=1
//         return self.ncc
// 
//     def dfs(self, k):
//         self.visited[k] = True
//         for p in self.g[k]:
//             if self.visited[p] == False:
//                 self.dfs(p)
// 
// def alternative_method(V, E):
//     return my_no_connected_components(build_graph(V,E)).find()

