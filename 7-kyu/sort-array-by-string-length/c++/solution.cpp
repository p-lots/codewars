#include <algorithm>
class Kata
{
public:
    std::vector<std::string> sortByLength(std::vector<std::string> array)
    {
        std::sort(array.begin(), array.end(), [](const auto &lhs, const auto &rhs) {
            return lhs.length() < rhs.length();
        });
        return array;
    }
};