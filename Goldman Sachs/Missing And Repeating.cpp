/*
Given an unsorted array arr of positive integers. One number a from the set [1, 2,....,n] is missing and one number b occurs twice in the array. Find numbers a and b.
Note: The test cases are generated such that there always exists one missing and one repeating number within the range [1,n].
*/

class Solution {
  public:
    vector<int> findTwoElement(vector<int>& arr) {
        // code here
        int n = arr.size()+1,p;
        for(int i=0;i<n-1;i++){
            p=arr[i]%n-1;
            arr[p]+=n;
        }
        vector<int> ans(2,0);
        for(int i=0;i<n-1;i++){
            p=arr[i]/n;
            if(p==0)    ans[1]=i+1;
            else if(p==2)   ans[0]=i+1;
        }
        return ans;
    }
};
