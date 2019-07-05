#include <algorithm>
#include <string>

class PlayPass
{
  public:
  static std::string playPass(const std::string &s, int n);
};

std::string PlayPass::playPass(const std::string &s, int n)
{
    std::string ret = s;
    for (unsigned i = 0; i < ret.length(); i++) {
        if (std::isalpha(ret[i])) {
            ret[i] += n;
            if (ret[i] > 90) ret[i] -= 26;
            if (i % 2 == 0) ret[i] = std::toupper(ret[i]);
            else ret[i] = std::tolower(ret[i]);
        }
        else if (std::isdigit(ret[i])) {
            ret[i] = (9 - (ret[i] - '0')) + '0';
        }
    }
    std::reverse(ret.begin(), ret.end());
    return ret;
}