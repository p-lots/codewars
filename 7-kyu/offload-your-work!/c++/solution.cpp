std::string workNeeded(int projectMinutes, std::vector<std::pair<int, int>> freelancers)
{
    int totalFreelancerMinutes = 0;
    for (const auto &pair : freelancers) {
        totalFreelancerMinutes += pair.first * 60 + pair.second;
    }
    int selfRequiredMinutes = std::max(0, projectMinutes - totalFreelancerMinutes);
    if (selfRequiredMinutes > 0) {
        int hoursNeeded = selfRequiredMinutes / 60;
        int minutesNeeded = selfRequiredMinutes % 60;
        return "I need to work " + std::to_string(hoursNeeded) + " hour(s) and " + std::to_string(minutesNeeded) + " minute(s)";
    }
    else return "Easy Money!";
}