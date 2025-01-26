/*
There are n cities numbered from 0 to n-1. Given the array edges where edges[i] = [fromi, toi, weighti] represents a bidirectional and weighted edge between cities fromi and toi, and given the integer distanceThreshold.
Return the city with the smallest number of cities that are reachable through some path and whose distance is at most distanceThreshold, If there are multiple such cities, return the city with the greatest number.
Notice that the distance of a path connecting cities i and j is equal to the sum of the edges' weights along that path.
*/

class Solution {
    public int findTheCity(int n, int[][] edges, int distanceThreshold) {
        int[][] adj_mat = new int[n][n];

        for (int i = 0; i < n; i++) {
            Arrays.fill(adj_mat[i], Integer.MAX_VALUE);
            adj_mat[i][i] = 0;
        }

        for (int[] e : edges) {
            adj_mat[e[0]][e[1]] = adj_mat[e[1]][e[0]] = e[2];
        }

        for (int k = 0; k < n; k++) {
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    if (adj_mat[i][k] != Integer.MAX_VALUE && adj_mat[k][j] != Integer.MAX_VALUE) {
                        adj_mat[i][j] = Math.min(adj_mat[i][j], adj_mat[i][k] + adj_mat[k][j]);
                    }
                }
            }
        }
        
        int ans = 0, minReachableCities = n;

        for (int i = 0; i < n; i++) {
            int reachableCities = 0;
            for (int j = 0; j < n; j++) {
                if (adj_mat[i][j] <= distanceThreshold) reachableCities++;
            }
            if (reachableCities <= minReachableCities) {
                ans = i;
                minReachableCities = reachableCities;
            }
        }
        
        return ans;
    }
}
