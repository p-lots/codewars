#include <iomanip>
#include <sstream>

class Kata
{
public:
    std::string height(int n)
    {
        if (n == 0) return "2000000.000";
        long double height = 2000000.0, height_ret = 0;
        for (int i = 0; i <= n; i++) {
            height_ret += height;
            height *= 0.4;
        }
       
        std::stringstream ret;
        ret << std::fixed << std::setprecision(3) << height_ret;
        return ret.str();
    }
};