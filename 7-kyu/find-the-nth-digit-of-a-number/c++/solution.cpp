#include <cmath>
#include <string>

int findDigit(int num, int nth)
{
    if (nth < 1) return -1;
    std::string n = std::to_string(std::abs(num));
    int index = n.length() - nth;
    if (index < 0) return 0;
    return n[index] - '0';
}