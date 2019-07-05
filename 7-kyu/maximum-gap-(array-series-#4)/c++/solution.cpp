#include <algorithm>
#include <cmath>
#include <vector>

using namespace std; 

int maxGap (vector <int> numbers)
{
  sort(numbers.begin(), numbers.end());
  int ret = numbers.front();
  for (unsigned i = 0; i < numbers.size() - 1; i++) {
    if (abs(numbers[i + 1] - numbers[i]) > ret) ret = abs(numbers[i + 1] - numbers[i]);
  }
  return ret;
}