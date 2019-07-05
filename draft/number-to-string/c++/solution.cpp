#include <sstream>

string numberToString(double n)
{
    stringstream ss;
    ss << n;
    if (ss.str().find("e") != string::npos) {
        ss.str("");
        ss << static_cast<int>(n);
    }
    return ss.str();
}