#include <map>
#include <sstream>

class StockList
{
public:
  static std::string stockSummary(std::vector<std::string> &lstOfArt, std::vector<std::string> &categories);
};

std::string StockList::stockSummary(std::vector<std::string> &lstOfArt, std::vector<std::string> &categories)
{
    if (lstOfArt.empty() || categories.empty()) return std::string("");
    std::map<char, int> code_counts;
    for (auto str : lstOfArt) {
        auto space_pos = str.find(" ");
        auto code = str.substr(0, space_pos);
        auto count = str.substr(space_pos + 1);
        code_counts[code[0]] += std::stoi(count);
    }
    std::stringstream ret;
    for (auto it = categories.begin(); it != categories.end(); it++) {
        auto str = *it;
        ret << "(" << str << " : " << code_counts[str[0]] << ")";
        if (it != categories.end() - 1) ret << " - ";
    }
    return ret.str();
}