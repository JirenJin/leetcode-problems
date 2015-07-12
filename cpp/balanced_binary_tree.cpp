# include<iostream>

using namespace std;
// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    bool isBalanced(TreeNode* root) {
        return getDepth(root)!=-1;
    }

    int getDepth(TreeNode* node) {
        if(!node) return 0;
        int l_depth = getDepth(node->left);
        if(l_depth==-1) return -1;
        int r_depth = getDepth(node->right);
        if(r_depth==-1) return -1;
        if(abs(l_depth-r_depth)>1) return -1;
        return max(l_depth, r_depth) + 1;
    }
};
