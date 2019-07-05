#include <cctype>
#include <map>
#include <string>
#include <vector>

std::map<char, char> get_key_map(std::string key)
{
    std::map<char, char> ret;
    for (unsigned i = 0; i < key.size(); i += 2) {
        auto pair = key.substr(i, 2);
        ret[pair[0]] = pair[1];
        ret[pair[1]] = pair[0];
    }
    return ret;
}

std::string encode (std::string str, std::string key)
{
    auto key_map = get_key_map(key);
    std::string ret = "";
    for (const char &c : str) {
        if (key_map[std::tolower(c)]) {
            ret += std::isupper(c) ? std::toupper(key_map[std::tolower(c)]) : key_map[c];
        }
        else ret += c;
    }
    return ret;
}

std::string decode (std::string str, std::string key)
{
    return encode(str, key);
}