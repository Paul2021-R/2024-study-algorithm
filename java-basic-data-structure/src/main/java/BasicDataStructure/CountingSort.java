package BasicDataStructure;

public class CountingSort {
    void sort(char arr[]) {
        int n = arr.length;

        // 결과 저장용
        char output[] = new char[n];

        // 초기화
        int count[] = new int[256];
        for (int i = 0; i < 256; ++i)
            count[i] = 0;

        // 각 문자 빈도 수를 센다
        for (int i = 0; i < n; ++i)
            ++count[arr[i]];

        // 카운트 배열을 변경하여, 각 문자의 최종 위치를 반영한다.
        for (int i = 1; i < 256; ++i)
            count[i] += count[i - 1];

        // 결과 빌드
        for (int i = n - 1; i >= 0; i--) {
            output[count[arr[i]] - 1] = arr[i];
            --count[arr[i]];
        }

        for (int i = 0; i < n; ++i)
            arr[i] = output[i];
    }

    public static void main(String[] args) {
        CountingSort countingSort = new CountingSort();
        char arr[] = {'g', 'e', 'e', 'k', 's', 'f', 'o', 'r', 'g', 'e', 'e', 'k', 's'};

        System.out.println("Original array:");
        for (char c : arr) {
            System.out.print(c + " ");
        }
        System.out.println();

        countingSort.sort(arr);

        System.out.println("Sorted array:");
        for (char c : arr) {
            System.out.print(c + " ");
        }
    }
}
