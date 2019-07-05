#include <algorithm>

int stray(std::vector<int> numbers)
{
    std::sort(numbers.begin(), numbers.end());
    auto first = numbers.front();
    auto it = std::find(numbers.begin() + 1, numbers.end(), first);
    if (it == numbers.end()) {
        return first;
    }
    for (it = numbers.begin() + 1; it != numbers.end(); it++) {
        if (first != *it) return *it;
    }
}