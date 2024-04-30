package BasicDataStructure;

public class TreeNode {
    int value;
    TreeNode left;
    TreeNode right;

    public TreeNode(int value) {
        this.value = value;
        this.left = null;
        this.right = null;
    }

    public void add(int value) {
        if (value < this.value) {
            if (this.left != null) {
                this.left.add(value);
            } else {
                this.left = new TreeNode(value);
            }
        } else {
            if (this.right != null) {
                this.right.add(value);
            } else {
                this.right = new TreeNode(value);
            }
        }
    }

    // 전위 순회
    public void preOrder() {
        System.out.print(this.value + " ");
        if (this.left != null) {
            this.left.preOrder();
        }
        if (this.right != null) {
            this.right.preOrder();
        }
    }

    // 중위 순회
    public void inOrder() {
        if (this.left != null) {
            this.left.inOrder();
        }
        System.out.print(this.value + " ");
        if (this.right != null) {
            this.right.inOrder();
        }
    }

    // 후위 순회
    public void postOrder() {
        if (this.left != null) {
            this.left.postOrder();
        }
        if (this.right != null) {
            this.right.postOrder();
        }
        System.out.print(this.value + " ");
    }
}