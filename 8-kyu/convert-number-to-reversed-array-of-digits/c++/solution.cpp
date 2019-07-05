std::vector<int> digitize(unsigned long n) 
{
    auto n_str = std::to_string(n);
    std::vector<int> ret;
    for (auto it = n_str.rbegin(); it != n_str.rend(); it++) {
        ret.push_back(*it - '0');
    }
    return ret;
}