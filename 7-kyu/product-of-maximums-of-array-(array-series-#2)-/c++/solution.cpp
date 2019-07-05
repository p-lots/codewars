#include <algorithm>
#include <vector>

using namespace std; 

int maxProduct (vector<int>numbers , int sub_size)
{
  std::sort(numbers.begin(), numbers.end());
  int ret = 1, count = 0;
  while (count < sub_size) {
    if (numbers.back() == 0) {
      numbers.pop_back();
      continue;
    }
    ret *= numbers.back();
    numbers.pop_back();
    count++;
  }
  return ret;
}