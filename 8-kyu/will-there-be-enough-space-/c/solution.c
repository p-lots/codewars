int enough(int cap, int on, int wait)
{
    int result = on + wait - cap;
    return result > 0 ? result : 0;
}