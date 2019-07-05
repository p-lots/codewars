using namespace std;

string arbitrate(const string& input, int n)
{
    string ret = "";
    bool found_master = false;
    for (const char &c : input) {
        if (c == '1' && found_master == false) {
            found_master = true;
            ret += "1";
        }
        else ret += "0";
    }
    return ret;
}