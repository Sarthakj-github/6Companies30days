/*
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.
Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.
Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.
*/

public class Codec {

    // Encodes a tree to a single string.
    public String serialize(TreeNode root) {
        if (root == null) return "null";
        
        StringBuilder ans = new StringBuilder();
        Queue<TreeNode> Q = new LinkedList<>();
        Q.add(root);
        
        while (!Q.isEmpty()) {
            TreeNode node = Q.poll();
            if (node != null) {
                ans.append(node.val).append(" ");
                Q.add(node.left);
                Q.add(node.right);
            } else {
                ans.append("null ");
            }
        }
        return ans.toString().trim();
    }

    // Decodes your encoded data to tree.
    public TreeNode deserialize(String data) {
        if (data.equals("null")) return null;
        
        String[] values = data.split(" ");
        TreeNode root = new TreeNode(Integer.parseInt(values[0]));
        Queue<TreeNode> Q = new LinkedList<>();
        Q.add(root);
        
        for (int i = 1; i < values.length; i++) {
            TreeNode node = Q.poll();
            if (!values[i].equals("null")) {
                node.left = new TreeNode(Integer.parseInt(values[i]));
                Q.add(node.left);
            }
            if (!values[++i].equals("null")) {
                node.right = new TreeNode(Integer.parseInt(values[i]));
                Q.add(node.right);
            }
        }
        return root;
    }
}
