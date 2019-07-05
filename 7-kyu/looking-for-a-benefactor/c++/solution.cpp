#include <cmath>
#include <stdexcept>
#include <numeric>
#include <vector>

class NewAverage
{
public:
   static long long newAvg(std::vector<double> &arr, double navg)
   {
       long long ret = std::ceil(navg * (arr.size() + 1) - std::accumulate(arr.begin(), arr.end(), 0.0));
       if (ret <= 0) throw std::logic_error("Logic error");
       return ret;
   }
};
