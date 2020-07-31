int sum_odd_digits(int n)
{
    if (n == 0) return 0;
    int last_digit = n % 10;
    if (last_digit % 2 == 1) return last_digit + sum_odd_digits(n / 10);
    else return sum_odd_digits(n / 10);
}