#include <array>
#include <vector>

using namespace std;

vector<int> get_digits(int n)
{
    vector<int> ret;
    while (n > 0) {
        ret.push_back(n % 10);
        n /= 10;
    }
    return ret;
}

array<int, 10> paint_letterboxes(int start, int end)
{
    array<int, 10> ret = { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
    for (int i = start; i <= end; i++) {
        auto digit_vec = get_digits(i);
        for (const auto &n : digit_vec) {
            ret[n]++;
        }
    }
    return ret;
}