// check whether any odd bit of x is 1
// it should return 1 if odd bit equal to 1 exists, 0 otherwise
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