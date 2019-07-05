#include <map>

std::vector<int> deleteNth(std::vector<int> arr, int n)
{
    std::map<int, int> value_counts;
    std::vector<int> ret;
    for (auto it = arr.begin(); it != arr.end(); it++) {
        if (value_counts[*it] < n) {
            ret.push_back(*it);
            value_counts[*it]++;
        }
    }
    return ret;
}