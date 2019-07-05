#include <cmath>

int hexToDec(std::string hexString)
{
    int radix = hexString.length() - 1, ret = 0;
    bool negative = false;
    for (const char &c : hexString) {
        int val = 0;
        if (c == '-') {
            radix--;
            negative = true;
            continue;
        }
        if (static_cast<int>(c) > 57) {
            // 'a' - 87 = 10, 'b' - 87 = 11, etc.
            if (static_cast<int>(c) > 70) val = static_cast<int>(c) - 87;
            else val = static_cast<int>(c) - 55;
        }
        else val = c - '0';
        ret += val * std::pow(16, radix);
        radix--;
    }
    return negative ? -ret : ret;
}