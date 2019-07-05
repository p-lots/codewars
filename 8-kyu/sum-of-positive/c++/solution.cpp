#include <numeric>
#include <vector>

int positive_sum (const std::vector<int> arr){
  return std::accumulate(arr.begin(), arr.end(), 0, [](int accum, int n) {
    if (n > 0) return accum + n;
    else return accum;
  });
}