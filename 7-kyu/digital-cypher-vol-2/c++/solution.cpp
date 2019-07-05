#include <string>

using namespace std;
class Kata
{
public:
	static string Decode(vector<int>, int);
};

string Kata::Decode(vector<int> code, int n)
{
    string n_digits = to_string(n);
    string ret(code.size(), ' ');
    for (unsigned i = 0; i < code.size(); i++) {
        unsigned n_digits_pos = i % n_digits.size();
        // 96 == '`', character before 'a'
        // therefore '`' + 1 == 'a', '`' + 2 == 'b', etc
        ret[i] = static_cast<char>(96 + code[i] - (n_digits[n_digits_pos] - '0'));
    }
    return ret;
}