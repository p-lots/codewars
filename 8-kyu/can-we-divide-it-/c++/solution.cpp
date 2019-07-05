#include <cmath>

bool isDivideBy(int number, int a, int b)
{
  return ((abs(number) % abs(a) == 0) && (abs(number) % abs(b) == 0));
}