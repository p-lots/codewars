#include <cmath>

using namespace std;

class IntSqRoot
{
    public:
    static long long intRac(long long n, long long guess)
    {
        long long ret = 0;
        while (true) {
            long long new_guess = (guess + n / guess) / 2;
            ret++;
            if (abs(guess - new_guess) < 1) break;
            guess = new_guess;
        }
        return ret;
    }
};
