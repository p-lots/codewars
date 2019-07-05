int solution(int number) 
{
    if (number <= 3) return 0;
    else if (number < 5) return 3;
    int ret = 0;
    for (unsigned i = 0; i < number; i++) {
        if (i % 3 == 0 || i % 5 == 0) ret += i;
    }
    return ret;
}