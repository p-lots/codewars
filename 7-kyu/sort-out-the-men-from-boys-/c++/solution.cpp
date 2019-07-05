#include <vector>
#include <algorithm>

std::vector<int> menFromBoys (std::vector<int> values)
{
    std::vector<int> evens, odds;
    for (const auto &n : values) {
        if (n % 2 == 0) evens.push_back(n);
        else odds.push_back(n);
    }
    std::sort(evens.begin(), evens.end());
    std::sort(odds.begin(), odds.end());
    evens.erase(std::unique(evens.begin(), evens.end()), evens.end());
    odds.erase(std::unique(odds.begin(), odds.end()), odds.end());
    std::reverse(odds.begin(), odds.end());
    evens.insert(evens.end(), odds.begin(), odds.end());
    return evens;
}