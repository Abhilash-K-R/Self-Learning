//100. Same Tree

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
bool isSameTree(struct TreeNode* p, struct TreeNode* q) {
    // Both nodes are NULL
    if (p == NULL && q == NULL)
        return true;

    // One node is NULL and the other is not
    if (p == NULL || q == NULL)
        return false;

    // Values are different
    if (p->val != q->val)
        return false;

    // Check left and right subtrees recursively
    return isSameTree(p->left, q->left) &&
           isSameTree(p->right, q->right);
}
