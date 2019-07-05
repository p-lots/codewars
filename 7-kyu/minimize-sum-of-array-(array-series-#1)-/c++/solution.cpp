#include <algorithm>
#include <vector>
using namespace std;

int minSum (vector<int>passed)
{
  sort(passed.begin(), passed.end());
  int ret = 0;
  int forward_counter = 0;
  int reverse_counter = passed.size() - 1;
  while (forward_counter < reverse_counter) {
    ret += passed[forward_counter] * passed[reverse_counter];
    forward_counter++;
    reverse_counter--;
  }
  return ret;
}