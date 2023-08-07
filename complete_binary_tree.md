# Tree properties
Tree is a data structure where all nodes point to a multiple noodes known as the *child* nodes. Which makes the given node a *parent* of all nodes it points to.

```mermaid
graph TD;
    A-->B;
    A-->C;
    B-->D;
    B-->E;
```

### Tree terminologies
**Root node** : The node with no parent.\
**Height of a node** : Maximum number of edges from the node to the farther leaf node.\
**Height of a tree** : Maximum number of edges from root to a leaf.\
**Levels in a tree** : Set of nodes in a tree having same height is called a level.\
**Leaf nodes** : All nodes with 0 children.

## Binary Tree
Tree with all nodes having at max 2 child nodes. 


## Strict Binary tree
Binary tree with all nodes having either 0 or exactly 2 nodes

## Complete binary tree
Binary tree with all the leaf nodes at the last or second last level with all the nodes in the last level being on the left side of the tree.

## Full binary tree
Binray tree with all levels having maximum possible nodes. Such a tree has nodes with exactly 2 children and leaf nodes at the same level.