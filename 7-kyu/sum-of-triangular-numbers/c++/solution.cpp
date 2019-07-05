int sumTriangularNumbers(int n) {
    int ret = 0;
    for (int i = 1; i <= n; i++) {
        ret += (i * (i + 1)) / 2;
    }
    return ret;
}