#include <bitset>
#include <vector>
using namespace std;

vector<int> showBits(int n){
    bitset<32> bs(n);
    auto bs_str = bs.to_string();
    vector<int> result;
    for (const auto &c : bs_str) {
        result.push_back(c == '0' ? 0 : 1);
    }
    return result;
}