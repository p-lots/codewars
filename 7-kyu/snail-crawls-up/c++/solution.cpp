int snail(int column, int day, int night)
{
    unsigned result = 0, i = 0;
    while (i < column) {
        i += day;
        result++;
        if (i >= column) return result;
        i -= night;
    }
    return result;
}