std::string no_space(std::string x)
{
    x.erase(std::remove_if(x.begin(), x.end(), [](char &c) { return std::isspace(c); }), x.end());
    return x;
}