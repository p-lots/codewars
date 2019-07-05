public class GCD {
    public static int compute(int x, int y) {
        for (;;) {
            if (x == 0) return y;
            y %= x;
            if (y == 0) return x;
            x %= y;
        }
    }
}