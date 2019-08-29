int findSum (int n)
{
    int ret = 0;
    for (unsigned i = 1; i <= n; i++) {
        if (i % 3 == 0 || i % 5 == 0) ret += i;
    }
    return ret;
}