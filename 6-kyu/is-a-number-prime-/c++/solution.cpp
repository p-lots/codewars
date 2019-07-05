#include <cmath>

bool isPrime(int num) {
  if (num < 2) return false;
  if (num == 2) return true;
  if (num % 2 == 0) return false;
  for (unsigned i = 3; i <= sqrt(num); i += 2) {
      if (num % i == 0) return false;
  }
  return true;
}