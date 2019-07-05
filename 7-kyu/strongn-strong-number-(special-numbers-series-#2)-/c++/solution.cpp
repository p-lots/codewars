#include <string>
using namespace std;

int fac(int n)
{
    int ret = 1;
    for (int i = 1; i <= n; i++) {
        ret *= i;
    }
    return ret;
}

string strong_num (int number)
{
    int factorial = 0, n = number;
    while (number > 0) {
        factorial += fac(number % 10);
        number /= 10;
    }
    return factorial == n ? "STRONG!!!!" : "Not Strong !!";
}