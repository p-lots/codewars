#include <algorithm>
#include <vector>

pair<int, int> findMostFrequent(forward_list<int> l)
{
    pair<int, int> output;
    vector<pair<int, int> > elem_counts;
    for (auto n : l) {
        auto it = find_if(elem_counts.begin(), elem_counts.end(), 
            [&n](const auto &p) { return n == p.first; });
        if (it == elem_counts.end()) {
            pair<int, int> ins = { n, 1 };
            elem_counts.push_back(ins);
        }
        else {
            it->second++;
        }
    }
    auto max_elem_it = max_element(elem_counts.begin(), elem_counts.end(), 
        [](const auto &lhs, const auto &rhs) { return lhs.second < rhs.second; });
    output = *max_elem_it;
    return output;
}