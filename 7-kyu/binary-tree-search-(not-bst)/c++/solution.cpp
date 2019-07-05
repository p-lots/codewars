struct Node {
  int val;
  Node *left = nullptr;
  Node *right = nullptr;
};

bool search(int n, Node *root)
{
    if (root == nullptr) return false;
    else if (root->val == n) return true;
    else {
        if (root->left == nullptr && root->right == nullptr && n != root->val) return false;
        return search(n, root->left) || search(n, root->right);
    }
}