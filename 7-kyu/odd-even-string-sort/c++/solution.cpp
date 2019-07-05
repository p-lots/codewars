using namespace std;

string sortMyString(const string &s)
{
    string first_half = "", second_half = "";
    for (unsigned i = 0; i < s.length(); i++) {
        if (i % 2 == 0) first_half.push_back(s[i]);
        else second_half.push_back(s[i]);
    }
    return string(first_half + " " + second_half);
}