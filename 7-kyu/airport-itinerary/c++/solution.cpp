bool operator!=(Route lhs, Route rhs)
{
    return lhs.in != rhs.in && lhs.out != rhs.out;
}

std::string itinerary(std::vector<Route> travel)
{
    std::string ret = "";
    auto prev_last = travel.front().out;
    for (auto route : travel) {
        std::string first = route.in, second = route.out;
        if (first != prev_last) ret += first;
        if (ret.back() != '-') ret += "-";
        ret += second;
        if (route != travel.back()) ret += "-";
        prev_last = second;
    }
    return ret;
}