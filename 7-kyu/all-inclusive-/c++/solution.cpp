#include <algorithm>
#include <string>
#include <vector>

class Rotations
{
public:
    static bool containAllRots(const std::string &strng, std::vector<std::string> &arr)
    {
        if (strng.empty()) return true;
        std::string strng_rot = strng;
        for (auto i = 0; i < strng_rot.length(); i++) {
            std::rotate(strng_rot.begin(), strng_rot.begin() + 1, strng_rot.end());
            if (std::find(arr.begin(), arr.end(), strng_rot) == arr.end()) return false;
        }
        return true;
    }
};
