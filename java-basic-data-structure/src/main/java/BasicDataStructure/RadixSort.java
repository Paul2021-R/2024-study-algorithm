package BasicDataStructure;

public class RadixSort {
    // 배열 arr[]의 원소들을 exp 기준으로 정렬하는 함수
    public static void countSort(int[] arr, int n, int exp) {
        int[] output = new int[n]; // 출력 배열
        int[] count = new int[10];
        java.util.Arrays.fill(count, 0);

        // exp에 해당하는 자릿수의 숫자를 카운트합니다.
        for (int i = 0; i < n; i++) {
            count[(arr[i] / exp) % 10]++;
        }

        // 카운트 배열을 변경하여 각 원소의 위치를 반영합니다.
        for (int i = 1; i < 10; i++) {
            count[i] += count[i - 1];
        }

        // 결과 배열을 빌드합니다.
        for (int i = n - 1; i >= 0; i--) {
            output[count[(arr[i] / exp) % 10] - 1] = arr[i];
            count[(arr[i] / exp) % 10]--;
        }

        // 결과 배열을 원래 배열에 복사합니다.
        for (int i = 0; i < n; i++) {
            arr[i] = output[i];
        }
    }

    // 기수 정렬 함수
    public static void radixSort(int[] arr, int n) {
        // 가장 큰 수를 찾아 자릿수를 결정합니다.
        int m = getMax(arr, n);

        // 모든 자릿수에 대해 카운팅 정렬을 수행합니다.
        for (int exp = 1; m / exp > 0; exp *= 10) {
            countSort(arr, n, exp);
        }
    }

    // 배열에서 최대값을 찾는 함수
    public static int getMax(int[] arr, int n) {
        int mx = arr[0];
        for (int i = 1; i < n; i++) {
            if (arr[i] > mx) {
                mx = arr[i];
            }
        }
        return mx;
    }

    // 메인 메서드: 기수 정렬을 테스트
    public static void main(String[] args) {
        int arr[] = {170, 45, 75, 90, 802, 24, 2, 66};
        int n = arr.length;
        radixSort(arr, n);
        System.out.println("Sorted array:");
        for (int i = 0; i < n; i++) {
            System.out.print(arr[i] + " ");
        }
    }
}
