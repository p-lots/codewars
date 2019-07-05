#include <algorithm>
#include <numeric>
#include <vector>

int summation(int num){
    std::vector<int> nums(num);
    std::iota(nums.begin(), nums.end(), 1);
    return std::accumulate(nums.begin(), nums.end(), 0);
}