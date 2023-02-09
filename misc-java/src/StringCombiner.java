import java.util.ArrayList;
import java.util.List;

public class StringCombiner {
    public static List<String> combine(List<String> strings) {
        List<String> result = new ArrayList<>();
        StringBuilder sb = new StringBuilder();
        for (String s : strings) {
            sb.append(s);
        }
        result.add(sb.toString());
        return result;
    }

    public static void main(String[] args) {
        List<String> strings = new ArrayList<>();
        strings.add("abc");
        strings.add("def");
        strings.add("ghi");
        List<String> combined = combine(strings);
        for (String s : combined) {
            System.out.println(s);
        }
    }
}
