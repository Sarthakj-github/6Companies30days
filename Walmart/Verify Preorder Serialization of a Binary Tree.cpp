/*
One way to serialize a binary tree is to use preorder traversal. When we encounter a non-null node, we record the node's value. If it is a null node, we record using a sentinel value such as '#'.
For example, the above binary tree can be serialized to the string "9,3,4,#,#,1,#,#,2,#,6,#,#", where '#' represents a null node.
Given a string of comma-separated values preorder, return true if it is a correct preorder traversal serialization of a binary tree.
It is guaranteed that each comma-separated value in the string must be either an integer or a character '#' representing null pointer.
You may assume that the input format is always valid.
For example, it could never contain two consecutive commas, such as "1,,3".
Note: You are not allowed to reconstruct the tree.
*/

class Solution {
public:
    bool isValidSerialization(string preorder) {
        int n=preorder.size();
        int c=1;
        for(int i=0;i<n;i++){
            if((i+1)==n || preorder[i+1]==','){
                if(c==0){
                    return false;
                }
                if(preorder[i]!='#'){
                    c+=2;
                }
                c-=1;
            }
        }
        if(c!=0){
            return false;
        }
        return true;
    }
};
