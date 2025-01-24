/*
You are given an m x n grid where each cell can have one of three values:
0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.
Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.
*/

class Solution {
    public int orangesRotting(int[][] grid) {
        int tot = 0,m = grid.length,n = grid[0].length;
        Queue<int[]> Q = new LinkedList<>();
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 2)    Q.add(new int[]{i, j, 0});
                if (grid[i][j] != 1)    tot++;
            }
        }
        int tm = 0;
        while (!Q.isEmpty()) {
            int[] point = Q.poll();
            int i = point[0],j = point[1],t = point[2];
            int[][] directions = {{0, -1}, {0, 1}, {1, 0}, {-1, 0}};
            for (int[] dir : directions) {
                int x = i + dir[0],y = j + dir[1];
                if (x >= 0 && x < m && y >= 0 && y < n && grid[x][y] == 1) {
                    Q.add(new int[]{x, y, t + 1});
                    grid[x][y] = 2; tot++;
                }
            }
            tm = Math.max(tm, t);
        }
        if (tot != (m * n)) return -1;
        return tm;
    }
}
