#include <algorithm>
#include <string>
#include <vector>

using namespace std; 


bool tidyNumber(int number)
{
    std::vector<int> digits;
    while (number > 0) {
        digits.push_back(number % 10);
        number /= 10;
    }
    std::reverse(digits.begin(), digits.end());
    for (unsigned i = 0; i < digits.size() - 1; i++) {
        if (digits[i + 1] < digits[i]) return false;
    }
    return true;
}