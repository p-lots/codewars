#include <algorithm>
#include <array>
#include <cctype>
#include <map>

using namespace std;

const map<string, string> month_lookup_table = {
    { "Jan", "01" }, { "Feb", "02" }, { "Mar", "03" },
    { "Apr", "04" }, { "May", "05" }, { "Jun", "06" },
    { "Jul", "07" }, { "Aug", "08" }, { "Sep", "09" },
    { "Oct", "10" }, { "Nov", "11" }, { "Dec", "12" }
};

string driver(const array<string, 5> &data)
{
    auto date_of_birth = data[3].substr(0, 2);
    auto month_to_lookup = data[3].substr(3, 3);
    auto month_of_birth = month_lookup_table.at(month_to_lookup);
    if (data[4] == "F") {
        month_of_birth[0] = (month_of_birth[0] == '0' ? '5' : '6');
    }
    auto year_of_birth_start_pos = data[3].find_last_of('-') + 1;
    auto year_of_birth = data[3].substr(year_of_birth_start_pos + 2);
    auto first_initial = data[0].substr(0, 1);
    string middle_initial = data[1].empty() ? "9" : data[1].substr(0, 1);
    string surname = data[2].substr(0, 5);
    while (surname.length() < 5) surname += "9";
    transform(surname.begin(), surname.end(), surname.begin(), 
        [](char c) { return isalpha(c) ? toupper(c) : c; });
    string ret = surname + year_of_birth.substr(0, 1) + month_of_birth
        + date_of_birth + year_of_birth.substr(1, 1) + first_initial
        + middle_initial + "9AA";
    return ret;
}