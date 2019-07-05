#include <vector>

int gcd(int a, int b)
{
  for (;;) {
    if (a == 0) return b;
    b %= a;
    if (b == 0) return a;
    a %= b;
  }
}

std::vector<int> relativelyPrime(int n, std::vector<int> list){
  std::vector<int> ret;
  for (const auto &number : list) {
    if (gcd(n, number) == 1) ret.push_back(number);
  }
  return ret;
}