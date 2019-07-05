#include <algorithm>
#include <cmath>

class Crisis
{
    public:
    static std::string helpZoom(std::vector<int> key);
};

std::string Crisis::helpZoom(std::vector<int> key)
{
    int sqrt = std::sqrt(key.size());
    if (sqrt * sqrt != key.size()) return "No";
    std::vector<int> first = std::vector<int>(key.begin(), key.begin() + key.size() / 2);
    std::vector<int> second = std::vector<int>(key.begin() + key.size() / 2, key.end());
    std::reverse(second.begin(), second.end());
    return std::equal(first.begin(), first.end(), second.begin()) ? "Yes" : "No";
}