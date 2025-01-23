/*
Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.
For example:
A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...
*/

class Solution {
    public String convertToTitle(int columnNumber) {
        int m=26,p;
        String ans = "";
        while(columnNumber>0){
            columnNumber--;
            p=columnNumber%m;
            ans = (char)(p+'A') + ans;
            columnNumber/=m;
        }
        return ans;
    }
}
