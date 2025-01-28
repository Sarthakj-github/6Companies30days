/*
Given a pattern containing only I's and D's. I for increasing and D for decreasing. Devise an algorithm to print the minimum number following that pattern. Digits from 1-9 and digits can't repeat.
*/

class Solution {
    int n;

    int trav(int i, String S, int ans, Set<Integer> st) {
        int fn = Integer.MAX_VALUE;
        if (i == n) return ans;
        for (int j = 1; j <= 9; j++) {
            if (S.charAt(i) == 'I' && ans % 10 < j && !st.contains(j)) {
                st.add(j);
                fn = Math.min(fn, trav(i + 1, S, ans * 10 + j, st));
                st.remove(j);
            } else if (S.charAt(i) == 'D' && ans % 10 > j && !st.contains(j)) {
                st.add(j);
                fn = Math.min(fn, trav(i + 1, S, ans * 10 + j, st));
                st.remove(j);
            }
        }
        return fn;
    }

    static String printMinNumberForPattern(String S) {
        Solution sol = new Solution();
        sol.n = S.length();
        Set<Integer> st = new HashSet<>();
        int result = Integer.MAX_VALUE;
        for (int p = 1; p <= 9; p++) {
            st.add(p);
            result = Math.min(result, sol.trav(0, S, p, st));
            st.remove(p);
        }
        return String.valueOf(result);
    }
}
