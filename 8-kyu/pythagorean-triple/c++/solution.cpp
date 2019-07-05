#include <algorithm>
#include <vector>

bool PythagoreanTriple(const int a, const int b, const int c)
{
  std::vector<int> vec = { a, b, c };
  std::sort(vec.begin(), vec.end());
  int a_sq = vec.at(0) * vec.at(0), b_sq = vec.at(1) * vec.at(1), c_sq = vec.at(2) * vec.at(2);
  return a_sq + b_sq == c_sq;
}