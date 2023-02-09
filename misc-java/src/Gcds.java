public class Gcds {
    public static int gcdOf(int[] numbers) {
        int result = numbers[0];
        for(int i = 1; i < numbers.length; i++){
            result = gcd(result, numbers[i]);
        }
        return result;
    }

    private static int gcd(final int a, final int b) {
        // System.out.printf("Finding GCD of %d and %d\n", a, b);
        if (b > a) {
            return gcd(b, a);
        }
        if (b == 0) {
            return a;
        }
        return gcd(b, a % b);
    }

    public static void main(String[] args) {
        int[] numbers = {15, 29, 44, 59, 74, 88, 103, 368};
        int result = gcdOf(numbers);
        System.out.println(result);
        // System.out.printf("Answer = %d\n", gcd(75, 100));
    }
}
