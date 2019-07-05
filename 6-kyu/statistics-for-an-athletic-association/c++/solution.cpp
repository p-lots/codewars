#include <algorithm>
#include <iomanip>
#include <vector>

typedef struct {
    int h;
    int m;
    int s;
} Time;

class Stat
{
public:
    static std::string stat(const std::string &strg);
    static Time median(std::vector<Time> times);
};

Time Stat::median(std::vector<Time> times)
{
    Time m1 = times.at(times.size() / 2), m2 = times.at((times.size() / 2) - 1);
    int med_s = m2.s + m1.s;
    int med_m = m2.m + m1.m;
    int med_h = m2.h + m1.h;
    if (med_s >= 60) {
        med_m += 1;
        med_s -= 60;
    }
    if (med_m >= 60) {
        med_h += 1;
        med_m -= 60;
    }
    int med_in_seconds = med_h * 60 * 60 + med_m * 60 + med_s;
    med_in_seconds /= 2;
    med_h = med_in_seconds / 3600;
    med_m = (med_in_seconds / 60) % 60;
    med_s = med_in_seconds % 60;
    return { med_h, med_m, med_s };
}

bool sort_func(const Time &lhs, const Time &rhs)
{
    if (lhs.h < rhs.h) return true;
    else if (lhs.h > rhs.h) return false;
    else {
        if (lhs.m < rhs.m) return true;
        else if (lhs.m > rhs.m) return false;
        else return lhs.s < rhs.s;
    }
}

std::string Stat::stat(const std::string &strng)
{
    if (strng.empty()) return "";
    std::vector<std::string> str_tokens;
    std::string::size_type start = 0, end;
    while ((end = strng.find(", ", start)) != std::string::npos) {
        str_tokens.push_back(strng.substr(start, end - start));
        start = end + 2;
    }
    str_tokens.push_back(strng.substr(start));
    std::vector<Time> times;
    for (const std::string s : str_tokens) {
        std::stringstream ss(s);
        std::string temp;
        Time t = { -1, -1, -1 };
        while (std::getline(ss, temp, '|')) {
            if (t.h == -1) t.h = std::stoi(temp);
            else if (t.m == -1) t.m = std::stoi(temp);
            else if (t.s == -1) t.s = std::stoi(temp);
        }
        times.push_back(t);
    }
    std::sort(times.begin(), times.end(), sort_func);
    Time med = (times.size() % 2 == 0 ? median(times) : times.at(times.size() / 2));
    int sum = 0, count = times.size();
    for (const auto time : times) {
        sum += (time.h * 60 * 60) + (time.m * 60) + time.s;
    }
    double avg_s = double(sum) / double(count);
    int avg_h = avg_s / 3600, avg_m = (int(avg_s) / 60) % 60, avg_s_int = int(avg_s) % 60;
    Time avg = { avg_h, avg_m, avg_s_int };
    Time min = *(std::min_element(times.begin(), times.end(), sort_func));
    Time max = *(std::max_element(times.begin(), times.end(), sort_func));
    int range_s = max.s - min.s;
    int range_m = max.m - min.m;
    if (range_s < 0) {
        range_m -= 1;
        range_s += 60;
    }
    int range_h = max.h - min.h;
    if (range_m < 0) {
        range_h -= 1;
        range_m += 60;
    }
    Time range = { range_h, range_m, range_s };
    std::stringstream ret_ss;
    ret_ss << "Range: "
        << std::setw(2) << std::setfill('0') << range.h << "|"
        << std::setw(2) << std::setfill('0') << range.m << "|"
        << std::setw(2) << std::setfill('0') << range.s
        << " Average: "
        << std::setw(2) << std::setfill('0') << avg.h << "|"
        << std::setw(2) << std::setfill('0') << avg.m << "|"
        << std::setw(2) << std::setfill('0') << avg.s
        << " Median: "
        << std::setw(2) << std::setfill('0') << med.h << "|"
        << std::setw(2) << std::setfill('0') << med.m << "|"
        << std::setw(2) << std::setfill('0') << med.s;
    return ret_ss.str();
}