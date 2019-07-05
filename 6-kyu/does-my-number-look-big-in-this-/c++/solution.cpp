#include <cmath>

bool narcissistic(int value)
{
    auto value_str = std::to_string(value);
    int sum = 0;
    for (const auto &n : value_str) {
        int digit = n - '0';
        sum += std::pow(digit, value_str.length());
    }
    return sum == value;
}