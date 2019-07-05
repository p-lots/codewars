#include <cmath>
#include <vector>

int thirstyIn(int water, std::vector<int> ageOfDweller)
{
    if (water < 0 || ageOfDweller.empty()) return -1;
    double litersPerDay = 0.0;
    for (int n : ageOfDweller) {
        if (n < 18) litersPerDay += 1.0;
        else if (n > 50) litersPerDay += 1.5;
        else litersPerDay += 2.0;
    }
    return water / std::ceil(litersPerDay);
}