#include <algorithm>
#include <cmath>
#include <numeric>
#include <string>
#include <vector>

class CountDig
{
public:
    static int nbDig(int n, int d)
    {
        std::vector<long long> numbers(n + 1);
        std::iota(numbers.begin(), numbers.end(), 0);
        std::transform(
            numbers.begin(), numbers.end(), numbers.begin(),
            [](const auto &num) { return std::pow(num, 2); });
        int count = 0;
        char d_char = d + '0';
        for (const auto num : numbers) {
            std::string num_str = std::to_string(num);
            count += std::count(num_str.begin(), num_str.end(), d_char);
        }
        return count;
    }
};
