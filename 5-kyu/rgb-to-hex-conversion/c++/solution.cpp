#include <cctype>
#include <iomanip>
#include <sstream>

class RGBToHex
{
  public:
  static std::string rgb(int r, int g, int b);
};

void clamp(int &n)
{
    n = std::min(std::max(n, 0), 255);
}

std::string int_to_hex(int n)
{
    clamp(n);
    std::stringstream ss;
    ss << std::setw(2) << std::setfill('0') << std::hex << n;
    std::string temp;
    ss >> temp;
    for (auto &c : temp)
        if (std::isalpha(c)) c = std::toupper(c);
    return temp;
}

std::string RGBToHex::rgb(int r, int g, int b)
{
    return int_to_hex(r) + int_to_hex(g) + int_to_hex(b);
}