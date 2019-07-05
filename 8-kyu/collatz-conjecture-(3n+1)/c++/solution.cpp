unsigned int hotpo(unsigned int n){
    int count = 0;
    while (n > 1) {
        n = (n % 2 == 0 ? n / 2 : n * 3 + 1);
        count++;
    }
    return count;
}