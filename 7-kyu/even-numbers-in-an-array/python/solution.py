#include <algorithm>
#include <vector>

std::vector<int> evenNumbers(std::vector<int> arr, int n) {
  auto it = arr.rbegin();
  std::vector<int> ret;
  while (n > 0 && it != arr.rend()) {
    if (*it % 2 == 0) {
      ret.push_back(*it);
      n--;
    }
    it++;
  }
  std::reverse(ret.begin(), ret.end());
  return ret;
}