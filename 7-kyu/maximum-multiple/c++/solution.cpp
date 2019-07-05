int maxMultiple(int divisor, int bound) 
{
    int ret = bound;
    while (!(ret % divisor == 0)) ret--;
    return ret;
}