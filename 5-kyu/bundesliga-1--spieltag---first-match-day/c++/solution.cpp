#include <algorithm>
#include <cctype>
#include <iostream>
#include <string>
#include <vector>

class Team
{
    std::string name;
    int goalsFor;
    int goalsAgainst;
    int matchesPlayed;
    int gamesWon;
    int gamesTied;
    int gamesLost;
    int points;
    int place;
public:
    Team(std::string n, int gF, int gA, int m, int gW, int gT, int gL, int p, int pl) :
        name(n), goalsFor(gF), goalsAgainst(gA), matchesPlayed(m), gamesWon(gW), gamesTied(gT),
        gamesLost(gL), points(p), place(pl) { }
    void setName(std::string n) { this->name = n; }
    std::string getName() const { return name; }
    void setGoalsFor(int gF) { this->goalsFor = gF; }
    int getGoalsFor() const { return goalsFor; }
    void setGoalsAgainst(int gA) { this->goalsAgainst = gA; }
    int getGoalsAgainst() const { return goalsAgainst; }
    void setMatchesPlayed(int m) { this->matchesPlayed = m; }
    int getMatchesPlayed() const { return matchesPlayed; }
    void setGamesWon(int gW) { this->gamesWon = gW; }
    int getGamesWon() const { return gamesWon; }
    void setGamesTied(int gT) { this->gamesTied = gT; }
    int getGamesTied() const { return gamesTied; }
    void setGamesLost(int gL) { this->gamesLost = gL; }
    int getGamesLost() const { return gamesLost; }
    void setPoints(int p) { this->points = p; }
    int getPoints() const { return points; }
    void setPlace(int pl) { this->place = pl; }
    int getPlace() const { return place; }
};

class Bundesliga
{
    std::vector<Team> team_data;
    void parseInput(std::vector<std::string>);
    void sortData();
    void addNewTeam(std::string, int, int);
    std::string format();
public:
    std::string table(std::vector<std::string> results);
};

std::string makeLower(std::string input)
{
    std::string ret;
    for (char c : input) {
        if (std::isalpha(c)) {
            ret.push_back(std::tolower(c));
        }
        else ret.push_back(c);
    }
    return ret;
}

bool sort_func(const Team &t1, const Team &t2)
{
    if (t1.getPoints() > t2.getPoints()) return true;
    else if (t2.getPoints() > t1.getPoints()) return false;
    int t1GoalDiff = t1.getGoalsFor() != -1 ? t1.getGoalsFor() - t1.getGoalsAgainst() : 0;
    int t2GoalDiff = t2.getGoalsFor() != -1 ? t2.getGoalsFor() - t2.getGoalsAgainst() : 0;
    if (t1GoalDiff > t2GoalDiff) return true;
    else if (t2GoalDiff > t1GoalDiff) return false;
    int t1Goals = t1.getGoalsFor() == -1 ? 0 : t1.getGoalsFor();
    int t2Goals = t2.getGoalsFor() == -1 ? 0 : t2.getGoalsFor();
    if (t1Goals > t2Goals) return true;
    else if (t2Goals > t1Goals) return false;
    return makeLower(t1.getName()) < makeLower(t2.getName());
}

std::string Bundesliga::table(std::vector<std::string> results)
{
    parseInput(results);
    sortData();
    return format();
}

void Bundesliga::addNewTeam(std::string name, int team_1_score, int team_2_score)
{
    int matchesPlayed = 0, gamesWon = 0, gamesTied = 0, gamesLost = 0, points = 0;
    if (team_1_score > team_2_score) {
        matchesPlayed = 1;
        gamesWon = 1;
        points = 3;
    }
    else if ((team_1_score == team_2_score) && (team_1_score != -1 && team_2_score != -1)) {
        matchesPlayed = 1;
        gamesTied = 1;
        points = 1;
    }
    else if (team_1_score < team_2_score) {
        matchesPlayed = 1;
        gamesLost = 1;
    }

    team_data.push_back(Team(name, team_1_score, team_2_score,
        matchesPlayed, gamesWon, gamesTied, gamesLost, points, 0));
}

std::string trimWS(std::string str)
{
    std::string::size_type start = 0, end = str.length() - 1;
    while (std::isspace(str[start])) start++;
    while (std::isspace(str[end])) end--;
    return str.substr(start, end - start + 1);
}

void Bundesliga::parseInput(std::vector<std::string> input)
{
    for (std::string s : input) {
        auto first_space = s.find(' ');
        std::string scores = s.substr(0, first_space);
        auto team_1_score_str = scores.substr(0, scores.find(':'));
        auto team_2_score_str = scores.substr(scores.find(':') + 1);
        int team_1_score = -1;
        int team_2_score = -1;
        if (team_1_score_str != "-") team_1_score = std::stoi(team_1_score_str);
        if (team_2_score_str != "-") team_2_score = std::stoi(team_2_score_str);
        auto team_sep = s.find('-', first_space);
        std::string team_1_name = trimWS(s.substr(first_space + 1,
            team_sep - first_space - 1));
        std::string team_2_name = trimWS(s.substr(team_sep + 1));
        addNewTeam(team_1_name, team_1_score, team_2_score);
        addNewTeam(team_2_name, team_2_score, team_1_score);
    }
}

void Bundesliga::sortData()
{
    std::sort(team_data.begin(), team_data.end(), sort_func);
    int actual_place = 1, team_place = 1;
    Team prev = team_data.front();
    team_data.front().setPlace(team_place);
    for (auto it = team_data.begin() + 1; it != team_data.end(); it++) {
        actual_place++;
        int t1GoalDiff = prev.getGoalsFor() != -1
            ? prev.getGoalsFor() - prev.getGoalsAgainst() : 0;
        int t2GoalDiff = it->getGoalsFor() != -1
            ? it->getGoalsFor() - it->getGoalsAgainst() : 0;
        int t1Goals = prev.getGoalsFor() != -1 ? prev.getGoalsFor() : 0;
        int t2Goals = it->getGoalsFor() != -1 ? it->getGoalsFor() : 0;
        if (((it->getPoints() == prev.getPoints())
            && t1GoalDiff == t2GoalDiff) && t1Goals == t2Goals) {
            it->setPlace(team_place);
        }
        else {
            team_place = actual_place;
            it->setPlace(team_place);
        }
        prev = *it;
    }
}

std::string Bundesliga::format()
{
    std::string ret;
    for (const auto team : team_data) {
        if (team.getPlace() < 10) ret += " ";
        ret += std::to_string(team.getPlace());
        ret += ". ";
        ret += team.getName();
        unsigned spaces = 30 - team.getName().length();
        ret += std::string(spaces, ' ');
        ret += std::to_string(team.getMatchesPlayed());
        ret += std::string(2, ' ');
        ret += std::to_string(team.getGamesWon());
        ret += std::string(2, ' ');
        ret += std::to_string(team.getGamesTied());
        ret += std::string(2, ' ');
        ret += std::to_string(team.getGamesLost());
        ret += std::string(2, ' ');
        int goalsFor = team.getGoalsFor() != -1 ? team.getGoalsFor() : 0;
        int goalsAgainst = team.getGoalsAgainst() != -1 ? team.getGoalsAgainst() : 0;
        ret += std::to_string(goalsFor) + ":"
            + std::to_string(goalsAgainst);
        ret += std::string(2, ' ');
        ret += std::to_string(team.getPoints());
        ret += "\n";
    }
    ret.pop_back();
    return ret;
}