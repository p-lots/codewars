#include <string>

std::string arithmeticSequenceElements(int a, int r, int n)
{
  std::string ret = std::to_string(a);
  for (int i = 1; i < n; i++) {
    a += r;
    ret += ", " + std::to_string(a);
  }
  return ret;
}