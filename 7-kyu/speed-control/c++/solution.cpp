#include <algorithm>
#include <cmath>
#include <iterator>
#include <numeric>

class GpsSpeed
{
public:
    static int gps(int s, std::vector<double> &x);
};

int GpsSpeed::gps(int s, std::vector<double> &x)
{
    if (x.empty()) return 0;
    std::vector<double> xx;
    std::adjacent_difference(x.begin(), x.end(), std::back_inserter(xx));
    std::transform(xx.begin(), xx.end(), xx.begin(), [&s](const double &n) { return (3600 * n) / s; });
    return std::floor(*(std::max_element(xx.begin(), xx.end())));
}