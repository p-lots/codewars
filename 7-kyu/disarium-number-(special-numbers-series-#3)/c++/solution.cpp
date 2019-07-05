#include <cmath>
#include <string>

using namespace std; 

string disariumNumber (int number )
{
  int len = std::ceil(std::log10(number));
  int sum = 0, n = number;
  while (number > 0) {
    sum += std::pow(number % 10, len);
    number /= 10;
    len--;
  }
  return n == sum ? "Disarium !!" : "Not !!";
}