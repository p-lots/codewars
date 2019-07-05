#include <algorithm>
#include <cctype>
#include <sstream>
#include <string>

class Rank
{
public:
    static std::string nthRank(const std::string &st, std::vector<int> &we, int n);
};

std::vector<std::string> tokenize(const std::string &line)
{
    std::vector<std::string> ret;
    std::stringstream ss(line);
    std::string temp;
    while (std::getline(ss, temp, ',')) {
        ret.push_back(temp);
    }
    return ret;
}

int getWinningNumber(const std::string &name, int weight)
{
    int sumOfRanks = name.length();
    for (const char &c : name) {
        char ch = std::toupper(c);
        sumOfRanks += ch - 'A' + 1;
    }
    return sumOfRanks * weight;
}

bool sortFunc(const std::pair<std::string, int> &lhs, const std::pair<std::string, int> &rhs)
{
    if (lhs.second == rhs.second) return lhs.first < rhs.first;
    else return lhs.second > rhs.second;
}

std::string Rank::nthRank(const std::string &st, std::vector<int> &we, int n)
{
    if (st.empty()) return "No participants";
    auto names = tokenize(st);
    if (n > names.size()) return "Not enough participants";
    std::vector<std::pair<std::string, int> > namesWithNumbers;
    for (unsigned i = 0; i < we.size(); i++) {
        auto name = names[i];
        auto winningNumber = getWinningNumber(name, we[i]);
        auto pair = std::make_pair(name, winningNumber);
        namesWithNumbers.push_back(pair);
    }
    std::sort(namesWithNumbers.begin(), namesWithNumbers.end(), sortFunc);
    return namesWithNumbers[n - 1].first;
}