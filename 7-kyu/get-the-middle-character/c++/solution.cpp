std::string get_middle(std::string input) 
{
    if (input.empty()) return "";
    return input.length() % 2 == 1 ? input.substr(input.length() / 2, 1) : input.substr(input.length() / 2 - 1, 2);
}