#include <algorithm>
#include <numeric>
#include <vector>

bool isAllPossibilities(std::vector<int> arr){
  if (arr.empty()) return false;
  std::vector<int> expected_arr(arr.size());
  std::iota(expected_arr.begin(), expected_arr.end(), 0);
  std::sort(arr.begin(), arr.end());
  return expected_arr == arr;
}