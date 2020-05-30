bool solution(std::string const &str, std::string const &ending)
{
    if (str.empty()) return false;
    else if (ending.empty()) return true;
    if (ending.length() > str.length()) return false;
    std::string str_end = str.substr(str.length() - ending.length());
    return str_end == ending;
}