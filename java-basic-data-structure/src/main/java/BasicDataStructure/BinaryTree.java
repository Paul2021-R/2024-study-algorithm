package BasicDataStructure;

public class BinaryTree {
    TreeNode root;

    public BinaryTree(int value) {
        root = new TreeNode(value);
    }

    public void add(int value) {
        addRecursive(root, value);
    }

    private TreeNode addRecursive(TreeNode current, int value) {
        if (current == null) {
            return new TreeNode(value);
        }

        if (value < current.value) {
            current.left = addRecursive(current.left, value);
        } else if (value > current.value) {
            current.right = addRecursive(current.right, value);
        } else {
            // 값이 같은 경우는 무시
            return current;
        }

        return current;
    }
}

