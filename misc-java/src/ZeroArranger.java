public class ZeroArranger {
    public static void arrange(int[] arr) {
        int zeroCount = 0;
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == 0) {
                zeroCount++;
            } else {
                arr[i - zeroCount] = arr[i];
            }
        }
        for (int i = arr.length - zeroCount; i < arr.length; i++) {
            arr[i] = 0;
        }
    }

    public static void main(String[] args) {
        int[] arr = {0, 2, 3, 0, 1, 0, 4, 5};
        arrange(arr);
        for (int i : arr) {
            System.out.print(i + " ");
        }
    }
}
