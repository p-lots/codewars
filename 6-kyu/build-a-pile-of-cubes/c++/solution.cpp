#include <cmath>

class ASum
{
  public:
  static long long findNb(long long m);
};

long long ASum::findNb(long long m)
{
    long long ret = 0LL;
    while (true) {
        ret++;
        m -= static_cast<long long>(std::pow(ret, 3));
        if (m == 0) return ret;
        else if (m < 0) return -1;
    }
}