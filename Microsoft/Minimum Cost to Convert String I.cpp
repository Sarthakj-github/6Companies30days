/*
You are given two 0-indexed strings source and target, both of length n and consisting of lowercase English letters. You are also given two 0-indexed character arrays original and changed, and an integer array cost, where cost[i] represents the cost of changing the character original[i] to the character changed[i].
You start with the string source. In one operation, you can pick a character x from the string and change it to the character y at a cost of z if there exists any index j such that cost[j] == z, original[j] == x, and changed[j] == y.
Return the minimum cost to convert the string source to the string target using any number of operations. If it is impossible to convert source to target, return -1.
Note that there may exist indices i, j such that original[j] == original[i] and changed[j] == changed[i].
*/
class Solution {
public:
    long long minimumCost(string source, string target, vector<char>& original, vector<char>& changed, vector<int>& cost) {
        int n = 26;
        int m = source.size();
        int l = original.size();
        long long ans = 0;

        vector<vector<int>> D(n, vector<int>(n, INT_MAX));

        for (int i = 0; i < l; i++) {
            int from_idx = original[i] - 'a';
            int to_idx = changed[i] - 'a';
            D[from_idx][to_idx] = min(D[from_idx][to_idx], cost[i]);
        }

        for (int i = 0; i < n; i++)
            D[i][i] = 0;

        for (int k = 0; k < n; k++)
            for (int i = 0; i < n; i++)
                for (int j = 0; j < n; j++)
                    if (D[i][k] != INT_MAX && D[k][j] != INT_MAX)
                        D[i][j] = min(D[i][j], D[i][k] + D[k][j]);

        for (int i = 0; i < m; i++) {
            if (source[i] != target[i]) {
                int s_idx = source[i] - 'a';
                int t_idx = target[i] - 'a';
                if (D[s_idx][t_idx] == INT_MAX)
                    return -1;
                ans += D[s_idx][t_idx];
            }
        }

        return ans;
    }
};
