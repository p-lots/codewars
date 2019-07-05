class Kata
{
public:
    static long total(long n);
};

long Kata::total(long n)
{
    return (n * (n + 1)) / 2;
}