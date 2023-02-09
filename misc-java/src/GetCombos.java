import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class GetCombos {

    public static List<String> combineListAndString(List<String> sList, String str) {
        List<String> result = new ArrayList<>();
        if (sList.isEmpty()) {
            sList =  Collections.singletonList("");
        }
        for (String s : sList) {
            for (char c : str.toCharArray()) {
                result.add(s+c);
            }
        }
        return result;
    }

    public static List<String> combineList(List<String> sList) {
        if (sList == null || sList.isEmpty()) {
            return Collections.emptyList();
        }
        List<String> baseList = combineList(sList.subList(0, sList.size() - 1));
        return combineListAndString(baseList, sList.get(sList.size() - 1));
    }

    public static void swap(int[] arr, int i, int j) {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }

    public static void moveZeros(int[] arr) {
        int i = 0;
        int j = arr.length - 1;
        for (;;) {
            while (i < j && arr[i] == 0) ++i;
            while (i < j && arr[j] != 0) --j;
            if (i < j) {
                swap(arr, i, j);
            } else {
                break;
            }
        }
    }


    public static void test(int[] arr) {
        System.out.println(Arrays.toString(arr));
        moveZeros(arr);
        System.out.println(Arrays.toString(arr));
    }


    public static void main(String[] args) {
        // test(new int[] {2, 4, 5, 0, -1, 7, -2, 0, 8, 0});
        System.out.println(combineList(Arrays.asList("abc", "12", "xyz")));
    }
}
