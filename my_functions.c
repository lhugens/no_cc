#include <stdio.h>
#include <stdlib.h>  // Include the header for malloc

struct Tuple{
    int first;
    int second;
};

void dfs(int k1, int visited[], int V[], int lengthV, struct Tuple *E, int lengthE){
    visited[k1] = 1;
    for(int e=0; e<lengthE; e++){
        int from = E[e].first-1;
        if(from == k1){
            int p = E[e].second-1; 
            if(visited[p] == 0){
                dfs(p, visited, V, lengthV, E, lengthE);
            }
        }
    }
}

int my_no_connected_components(int V[], int lengthV, struct Tuple* E, int lengthE){
    // init
    int ncc = 0;

        // create visited array
    int *visited = malloc(lengthV * sizeof(int)); // Allocate memory for the visited array
    if (visited == NULL) { // Handle memory allocation error if necessary
        return -1; // Indicate an error
    }
    for(int i=0; i<lengthV; i++){
        visited[i] = 0;
    }
    //
    // find
    for(int k=0; k<lengthV; k++){
        if(visited[k] == 0){
            dfs(k, visited, V, lengthV, E, lengthE);
            ncc++;
        }
    }
    //int sum = 0;
    //for(int i=0; i<lengthV; i++){
    //    sum += visited[i];
    //}

    return ncc;
}
