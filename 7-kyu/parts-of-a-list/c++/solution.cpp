#include <string>
#include <utility>
#include <vector>

class PartList
{
public:
static std::vector<std::pair <std::string, std::string>> partlist(std::vector<std::string> &arr)
{
    std::vector<std::pair <std::string, std::string>> ret;
    for (auto it = arr.begin(); it != arr.end(); it++) {
        std::string first_half = "";
        for (auto it2 = arr.begin(); it2 != it + 1; it2++) {
            first_half += *it2;
            if (it2 != it) first_half += " ";
        }
        std::string second_half = "";
        for (auto it2 = it + 1; it2 != arr.end(); it2++) {
            second_half += *it2;
            if (it2 != arr.end() - 1) second_half += " ";
        }
        if (it != arr.end() - 1) ret.push_back(std::make_pair(first_half, second_half));
    }
    return ret;
}
};