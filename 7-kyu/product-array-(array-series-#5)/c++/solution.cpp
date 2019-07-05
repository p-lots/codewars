#include <vector>

using namespace std; 

vector<int> productArray (vector<int> numbers)
{
  unsigned product = 1;
  for (const auto &n : numbers) {
    product *= n;
  }
  vector<int> ret(numbers.size(), product);
  for (unsigned i = 0; i < ret.size(); i++) {
      ret[i] = product / numbers[i];
  }
  return ret;
}