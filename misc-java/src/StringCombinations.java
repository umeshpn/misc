import java.util.*;

public class StringCombinations {
    public static List<String> getCombinations(List<String> strings) {
        List<String> combinations = new ArrayList<>();
        if (strings == null || strings.isEmpty()) {
            return combinations;
        }
        int[] indexes = new int[strings.size()];
        while (indexes[0] < strings.get(0).length()) {
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < strings.size(); i++) {
                sb.append(strings.get(i).charAt(indexes[i]));
            }
            combinations.add(sb.toString());
            indexes[strings.size() - 1]++;
            for (int i = strings.size() - 1; i > 0; i--) {
                if (indexes[i] == strings.get(i).length()) {
                    indexes[i] = 0;
                    indexes[i - 1]++;
                }
            }
        }
        return combinations;
    }

    public static void main(String[] args) {
        test(null);
        test(Arrays.asList());
        test(Arrays.asList("abc"));
        test(Arrays.asList("abc", "de", "xyz"));
        test(Arrays.asList("aaa", "bb", "ccc"));
    }

    private static void test(final List<String> slist) {
        System.out.println("\nInput : " + slist);
        final List<String> out = getCombinations(slist);
        System.out.println("Output : " + out);
    }
}
