std::string repeater(std::string str, int n)
{
    std::string ret = "";
    for (unsigned i = 0; i < n; i++) {
        ret += str;
    }
    return ret;
}