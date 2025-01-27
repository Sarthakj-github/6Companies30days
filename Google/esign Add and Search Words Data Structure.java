/*
Design a data structure that supports adding new words and finding if a string matches any previously added string.
Implement the WordDictionary class:
WordDictionary() Initializes the object.
void addWord(word) Adds word to the data structure, it can be matched later.
bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.
*/

class TrieNode {
    TrieNode[] d;
    int end;

    TrieNode() {
        this.d = new TrieNode[26];
        this.end = 0;
    }
}

class WordDictionary {
    TrieNode root;

    public WordDictionary() {
        this.root = new TrieNode();
    }

    public void addWord(String word) {
        int n = word.length();
        TrieNode temp = root;
        for (int i = 0; i < n; i++) {
            char p = word.charAt(i);
            int index = p - 'a';
            if (temp.d[index] == null) {
                temp.d[index] = new TrieNode();
            }
            temp = temp.d[index];
        }
        temp.end += 1;
    }

    public boolean search(String word) {
        return trav(word, 0, root);
    }

    boolean trav(String word, int i, TrieNode temp) {
        if (i == word.length()) {
            return temp.end != 0;
        }
        char p = word.charAt(i);
        if (p == '.') {
            for (int j = 0; j < 26; j++) {
                if (temp.d[j] != null && trav(word, i + 1, temp.d[j])) {
                    return true;
                }
            }
        } else {
            int index = p - 'a';
            if (temp.d[index] == null) {
                return false;
            }
            return trav(word, i + 1, temp.d[index]);
        }
        return false;
    }
}
