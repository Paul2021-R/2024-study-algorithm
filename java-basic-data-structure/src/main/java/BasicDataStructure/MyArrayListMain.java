package BasicDataStructure;

public class MyArrayListMain {
    public static void main(String[] args) {
        MyArrayList<Integer> list = new MyArrayList<>();
        list.add(1);
        list.add(2);
        list.add(3);
        list.add(4);

        for (int i = 0; i < list.getSize(); i++){
            System.out.println(list.get(i));
        }
    }
}
