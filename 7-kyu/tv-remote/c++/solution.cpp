#include <map>
#include <utility>
#include <vector>

using namespace std;

const vector<vector<char> > lookup_table = {
    { 'a', 'b', 'c', 'd', 'e', '1', '2', '3' },
    { 'f', 'g', 'h', 'i', 'j', '4', '5', '6' },
    { 'k', 'l', 'm', 'n', 'o', '7', '8', '9' },
    { 'p', 'q', 'r', 's', 't', '.', '@', '0' },
    { 'u', 'v', 'w', 'x', 'y', 'z', '_', '/' }
};

void make_lookup_map(map<char, pair<int, int> > &m)
{
    for (unsigned i = 0; i < lookup_table.size(); i++) {
        for (unsigned j = 0; j < lookup_table[i].size(); j++) {
            m[lookup_table[i][j]] = make_pair(i, j);
        }
    }
}

int tv_remote(const string &word)
{
    map<char, pair<int, int> > lookup_map;
    make_lookup_map(lookup_map);
    char prev_letter = 'a';
    int ret = 0;
    for (const auto &c : word) {
        auto prev_letter_pair = lookup_map[prev_letter];
        auto curr_letter_pair = lookup_map[c];
        int dist = (abs(prev_letter_pair.first - curr_letter_pair.first) + abs(prev_letter_pair.second - curr_letter_pair.second));
        ret += dist + 1;
        prev_letter = c;
    }
    return ret;
}