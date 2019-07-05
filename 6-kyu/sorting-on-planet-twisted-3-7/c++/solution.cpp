#include <algorithm>
#include <string>
#include <vector>
using namespace std;

void translate(vector <int> &ret)
{
    for (int &n : ret) {
        auto n_str = to_string(n);
        char new_value = n_str.front();
        replace_if(n_str.begin(), n_str.end(), [&new_value](const char &c) {
            if (c == '3') new_value = '7';
            else if (c == '7') new_value = '3';
            else new_value = c;
            return c == '3' || c == '7';
        }, new_value);
        n = std::stoi(n_str);
    }
}

vector <int> sortTwisted37 (vector <int> numbers) {
    auto ret = numbers;
    translate(ret);
    sort(ret.begin(), ret.end());
    translate(ret);
    return ret;
}