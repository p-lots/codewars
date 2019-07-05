#include <vector>

class Operarray
{
public:
    static long long gcdi(long long x, long long y);
    static long long lcmu(long long a, long long b);
    static long long som(long long a, long long b);
    static long long maxi(long long a, long long b);
    static long long mini(long long a, long long b);
    // your high order function oper
    static long long oper(std::function<long long(long long, long long)> func, long long a, long long b);
    // your high order function operArray
    static std::vector<long long> operArray(std::function<long long(long long, long long)> func, std::vector<long long> &arr, long long init);
};

long long Operarray::gcdi(long long x, long long y)
{
    x = std::llabs(x);
    y = std::llabs(y);
    for (;;) {
        if (x == 0) return y;
        y %= x;
        if (y == 0) return x;
        x %= y;
    }
}

long long Operarray::lcmu(long long a, long long b)
{
    a = std::llabs(a);
    b = std::llabs(b);
    auto temp = Operarray::gcdi(a, b);
    return temp ? (a / temp * b) : 0;
}

long long Operarray::som(long long a, long long b)
{
    return a + b;
}

long long Operarray::maxi(long long a, long long b)
{
    return std::max(a, b);
}

long long Operarray::mini(long long a, long long b)
{
    return std::min(a, b);
}

long long Operarray::oper(std::function<long long(long long, long long)> func, long long a, long long b)
{
    return func(a, b);
}

std::vector<long long> Operarray::operArray(std::function<long long(long long, long long)> func, std::vector<long long> &arr, long long init)
{
    auto first = Operarray::oper(func, init, arr.front());
    std::vector<long long> ret;
    ret.push_back(first);
    for (auto arr_it = arr.begin() + 1; arr_it != arr.end(); arr_it++) {
        ret.push_back(Operarray::oper(func, ret.back(), *arr_it));
    }
    return ret;
}
