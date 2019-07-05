int sequenceSum(int start, int end, int step)
{
    if (start > end) return 0;
    int ret = 0;
    for (unsigned i = start; i <= end; i += step) {
        ret += i;
    }
    return ret;
}