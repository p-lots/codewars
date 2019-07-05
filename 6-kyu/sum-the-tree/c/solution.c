#include <stddef.h>

struct node
{
  int value;
  struct node* left;
  struct node* right;
};


int sumTheTreeValues(struct node* root)
{
    if (root->left == NULL && root->right == NULL) return root->value;
    else if (root->left == NULL) return root->value + sumTheTreeValues(root->right);
    else if (root->right == NULL) return root->value + sumTheTreeValues(root->left);
    else return root->value + sumTheTreeValues(root->left) + sumTheTreeValues(root->right);
}