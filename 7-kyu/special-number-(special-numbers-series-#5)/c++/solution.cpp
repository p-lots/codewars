#include <string>

using namespace std; 

string specialNumber (int number)
{
  while (number > 0) {
    if ((number % 10) > 5) return "NOT!!";
    number /= 10;
  }
  return "Special!!";
}