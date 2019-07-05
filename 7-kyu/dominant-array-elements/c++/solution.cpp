#include <algorithm>
#include <vector>

std::vector<int> solve(std::vector<int> array)
{
  std::vector<int> ret;
  ret.push_back(array.back());
  for (int i = array.size() - 2; i >= 0; i--) {
    int max = array[i];
    bool is_max = true;
    for (unsigned j = i; j < array.size(); j++) {
      if (j != i) {
        if (max > array[j]) is_max = true;
        else {
          is_max = false;
          break;
        }
      }
    }
    if (is_max) ret.push_back(max);
  }
  std::reverse(ret.begin(), ret.end());
  return ret;
}