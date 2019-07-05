#include <set>
#include <string>

std::string removeDuplicateWords(const std::string& str)
{
    if (str.empty()) return "";
    else if (str.find(" ") == std::string::npos) return str;
    std::string::size_type start = 0, end;
    std::set<std::string> str_set;
    std::string ret = "", temp;
    while ((end = str.find(" ", start)) != std::string::npos) {
        temp = str.substr(start, end - start);
        if (str_set.count(temp) == 0) {
            str_set.insert(temp);
            ret += temp + " ";
        }
        start = end + 1;
    }
    temp = str.substr(start);
    if (str_set.count(temp) == 0) ret += temp;
    else ret.pop_back();
    return ret;
}