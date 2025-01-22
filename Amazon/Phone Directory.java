/*
Given a list of contacts contact[] of length n where each contact is a string which exist in a phone directory and a query string s. The task is to implement a search query for the phone directory. Run a search query for each prefix p of the query string s (i.e. from  index 1 to |s|) that prints all the distinct contacts which have the same prefix as p in lexicographical increasing order. Please refer the explanation part for better understanding.
Note: If there is no match between query and contacts, print "0".
*/


class TrieNode {
    TrieNode[] d;
    ArrayList<String> A;

    TrieNode() {
        this.d = new TrieNode[26];
        this.A = new ArrayList<>();
    }
}

class Solution {
    static TrieNode root;

    static ArrayList<ArrayList<String>> displayContacts(int n, String contact[], String s) {
        root = new TrieNode();
        contact = distinct(contact);
        for (String word : contact) {
            insert(word);
        }
        
        return startsWith(s);
    }

    public static void insert(String word) {
        int length = word.length();
        TrieNode temp = root;
        for (int i = 0; i < length; i++) {
            char ch = word.charAt(i);
            int index = ch - 'a';
            if (temp.d[index] == null) {
                temp.d[index] = new TrieNode();
            }
            temp.d[index].A.add(word);
            temp = temp.d[index];
        }
    }

    public static ArrayList<ArrayList<String>> startsWith(String prefix) {
        TrieNode temp = root;
        ArrayList<ArrayList<String>> ans = new ArrayList<>();
        int i = 0, length = prefix.length();
        
        while (i < length) {
            int index = prefix.charAt(i) - 'a';
            if (temp.d[index] == null) break;
            ArrayList<String> app = new ArrayList<>(temp.d[index].A);
            Collections.sort(app);
            ans.add(app);
            temp = temp.d[index];
            i++;
        }

        while (i++ < length) {
            ans.add(new ArrayList<>(List.of("0")));
        }
        
        return ans;
    }
    
    public static String[] distinct(String[] contact) {
        Set<String> set = new HashSet<>();
        for (String word : contact) {
            set.add(word);
        }
        return set.toArray(new String[0]);
    }
    
}
