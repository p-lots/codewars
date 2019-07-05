#include <string>
#include <vector>

class Kata
{
public:
    static std::vector<int> Encode(std::string str, int n);
};

std::vector<int> vectorize(int n)
{
    std::vector<int> ret;
    auto n_str = std::to_string(n);
    for (auto it = n_str.begin(); it != n_str.end(); it++) {
        ret.push_back(*it - '0');
    }
    return ret;
}

std::vector<int> Kata::Encode(std::string str, int n)
{
    std::vector<int> n_tokens = vectorize(n), ret;
    auto n_tokens_it = n_tokens.begin();
    for (const char &c : str) {
        // c - '`';
        int c_num = c - '`';
        ret.push_back(c_num + *n_tokens_it);
        n_tokens_it++;
        if (n_tokens_it == n_tokens.end()) n_tokens_it = n_tokens.begin();
    }
    return ret;
}