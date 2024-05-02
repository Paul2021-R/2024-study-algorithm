package BasicDataStructure;

public class BubbleSort {
    void bubleSort(int arr[]) {
        int n = arr.length;
        // 핵심적인 N^2 의 시간 복잡도는 이중 루프에서 발생한다.
        for (int i = 0; i < n - 1; i++) {
            for (int j = 0; j < n - 1; j++) {
                if (arr[j] > arr[j + 1]) {
                    int temp = arr[j];
                    arr[j] = arr[j+1];
                    arr[j+1] = temp;
                }
            }
        }
    }

    void printArray(int arr[]) {
        for (int i = 0; i < arr.length; i++)
            System.out.print(arr[i] + " ");
        System.out.println();
    }

    public static void main(String args[]) {
        BubbleSort ob = new BubbleSort();
        int arr[] = {64, 34, 25, 12, 22, 11, 90};
        ob.bubleSort(arr);
        System.out.println("Sorted array");
        ob.printArray(arr);
    }
}
