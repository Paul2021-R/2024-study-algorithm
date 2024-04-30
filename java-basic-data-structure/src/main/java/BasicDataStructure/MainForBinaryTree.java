package BasicDataStructure;

public class MainForBinaryTree {
    public static void main(String[] args) {
        BinaryTree tree = new BinaryTree(40);
        tree.add(20);
        tree.add(60);
        tree.add(10);
        tree.add(30);
        tree.add(50);
        tree.add(70);

        System.out.println("Pre-order traversal:");
        tree.root.preOrder();
        System.out.println();

        System.out.println("In-order traversal:");
        tree.root.inOrder();
        System.out.println();

        System.out.println("Post-order traversal:");
        tree.root.postOrder();
        System.out.println();
    }
}
