/*
Given a string s, Your task is to complete the function encode that returns the run length encoded string for the given string.
eg if the input string is “wwwwaaadexxxxxx”, then the function should return “w4a3d1e1x6″.
You are required to complete the function encode that takes only one argument the string which is to be encoded and returns the encoded string.
*/

class Solution {
  public:
    string encode(string s) {
        // code here
        string ans="";
        int i=0,n=s.length(),j;
        while(i<n){
            j=i+1;
            while(j<n and s[j]==s[i]){
                j++;
            }
            ans+=s[i]+to_string(j-i);
            i=j;
        }
        return ans;
    }
};
