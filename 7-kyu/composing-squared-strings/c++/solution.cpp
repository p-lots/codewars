#include <sstream>
#include <string>
#include <vector>

class ComposeSqStrings
{
private:
    static std::vector<std::string> tokenize(std::string str);
public:
    static std::string compose(const std::string &s1, const std::string &s2);
};

std::vector<std::string> ComposeSqStrings::tokenize(std::string str)
{
    std::vector<std::string> ret;
    std::stringstream ss(str);
    std::string temp;
    while (std::getline(ss, temp)) {
        ret.push_back(temp);
    }
    return ret;
}

std::string ComposeSqStrings::compose(const std::string &s1, const std::string &s2)
{
    auto tokens_s1 = tokenize(s1), tokens_s2 = tokenize(s2);
    auto tokens_s1_it = tokens_s1.begin();
    auto tokens_s2_rit = tokens_s2.rbegin();
    std::string ret = "";
    int char_counter = 1;
    while (tokens_s1_it != tokens_s1.end() && tokens_s2_rit != tokens_s2.rend()) {
        std::string line = "";
        line += tokens_s1_it->substr(0, char_counter);
        line += tokens_s2_rit->substr(0, tokens_s2_rit->size() - char_counter + 1);
        ret += line + "\n";
        char_counter++;
        tokens_s1_it++;
        tokens_s2_rit++;
    }
    ret.pop_back();
    return ret;
}