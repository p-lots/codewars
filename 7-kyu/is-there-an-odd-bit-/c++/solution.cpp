int any_odd(unsigned x)
{
    unsigned i = 0;
    while (x > 0) {
        if (i % 2 == 1 && x & 1) return 1;
        i++;
        x >>= 1;
    }
    return 0;
}