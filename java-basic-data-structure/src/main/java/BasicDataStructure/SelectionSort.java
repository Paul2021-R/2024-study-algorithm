package BasicDataStructure;

public class SelectionSort {
    public static void sort(int[] array) {
        for (int i = 0 ; i < array.length - 1; i++) {
            // 최소 값을 찾기 위해 시작 인덱스를 지정한다.
            int minIndex = i;
            for (int j = i + 1; j <array.length; j++) {
                if (array[j] < array[minIndex]) {
                    minIndex = j;
                }
            }
            int temp = array[i];
            array[i] = array[minIndex];
            array[minIndex] = temp;
        }
    }
    public static void main(String[] args) {
        int[] array = {64, 34, 25, 12, 22, 11 ,11,11, 11, 90};
        sort(array);
        System.out.println("Sorted array: ");
        for (int i : array) {
            System.out.print(i + " ");
        }
    }
}
