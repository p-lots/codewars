#include <vector>

int count_sheep(std::vector<bool> arr) 
{
    int ret = 0;
    for (bool b : arr) {
        ret += (b ? 1 : 0);
    }
    return ret;
}

