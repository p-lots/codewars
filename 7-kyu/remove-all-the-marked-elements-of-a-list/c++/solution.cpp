#include <vector>

std::vector<int> remove_values(std::vector<int> integers, std::vector<int> values)
{
    for (const auto &n : values) {
        integers.erase(std::remove(integers.begin(), integers.end(), n), integers.end());
    }
    return integers;
}