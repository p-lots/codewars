#include <cmath>

bool is_square(int n)
{
    if (n < 0) return false;
    double result = std::sqrt(static_cast<double>(n));
    if (std::fmod(result, 1.0) == 0.0) return true;
    return false;
}