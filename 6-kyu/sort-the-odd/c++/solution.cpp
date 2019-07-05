#include <algorithm>

class Kata
{
public:
    std::vector<int> sortArray(const std::vector<int> array)
    {
        if (array.empty()) return array;
        std::vector<int> odd_arr;
        for (const int n : array) {
            if (n % 2 == 1) {
                odd_arr.push_back(n);
            }
        }
        std::sort(odd_arr.begin(), odd_arr.end());
        auto ret = array;
        auto odd_arr_it = odd_arr.begin();
        for (int &n : ret) {
            if (n % 2 == 1) {
                n = *odd_arr_it;
                odd_arr_it++;
            }
        }
        return ret;
    }
};