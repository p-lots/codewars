#include <cmath>

int layers(int n)
{
  if (n == 1) return 1;
  int pow = 1, pow_res = 1, ret = 0;
  while (pow_res < n) {
    pow_res = std::pow(pow, 2);
    ret++;
    pow += 2;
  }
  return ret;
}