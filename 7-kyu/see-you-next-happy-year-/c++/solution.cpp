#include <vector>

bool isHappyYear(unsigned short int year)
{
    std::vector<int> year_vec;
    while (year > 0) {
        year_vec.push_back(year % 10);
        year /= 10;
    }
    for (const auto &n : year_vec) {
        if (std::count(year_vec.begin(), year_vec.end(), n) > 1) return false;
    }
    return true;
}

unsigned short int nextHappyYear (unsigned short int year)
{
    if (isHappyYear(year)) year++;
    while (!isHappyYear(year)) {
        year++;
    }
    return year;
}