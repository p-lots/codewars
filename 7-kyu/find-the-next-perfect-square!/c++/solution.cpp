#include <cmath>

long int findNextSquare(long int sq) {
  long double square_root = std::sqrt(sq);
  if (std::fmod(square_root, 1.0) > 0.0) return -1;
  return std::pow(square_root + 1, 2);
}