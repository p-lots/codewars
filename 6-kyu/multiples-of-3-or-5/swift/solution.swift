int solution(int number) 
{
    if (number <= 3) return 0;
    else if (number == 4 || number == 5) return 3;
    int ret = 0;
    bool arr[number];
    for (unsigned i = 0; i < number; i++) {
        arr[i] = false;
    }
    for (unsigned i = 3; i < number; i += 3) {
        arr[i] = true;
    }
    for (unsigned i = 5; i < number; i += 5) {
        arr[i] = true;
    }
    for (unsigned i = 3; i < number; i++) {
        if (arr[i]) ret += i;
    }
    return ret;
}