#include <cmath>
#include <string>

std::string jumpingNumber(int number)
{
    int prev = number % 10;
    number /= 10;
    while (number > 0) {
        int curr = number % 10;
        if (std::abs(curr - prev) != 1) return "Not!!";
        prev = curr;
        number /= 10;
    }
    return "Jumping!!";
}