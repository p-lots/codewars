#include <algorithm>
#include <sstream>
#include <string>
#include <utility>
#include <vector>

typedef std::pair<std::string, int> scorePair;
typedef std::vector<scorePair> scorePairVec;

int getScore(const std::string &word)
{
  int ret = 0;
  for (const auto &c : word) {
    ret += static_cast<int>(c - 'a' + 1);
  }
  return ret;
}

std::vector<std::string> tokenize(const std::string &line)
{
  std::vector<std::string> ret;
  std::stringstream ss(line);
  std::string temp;
  while (std::getline(ss, temp, ' '))
    ret.push_back(temp);
  return ret;
}

std::string highestScoringWord(const std::string &str)
{
  auto tokens = tokenize(str);
  scorePairVec vec;
  for (const auto &word : tokens) {
    vec.push_back(std::make_pair(word, getScore(word)));
  }
  auto max_elem = *std::max_element(vec.begin(), vec.end(), 
    [](const scorePair &lhs, const scorePair &rhs) {
      return lhs.second < rhs.second;
    });
  return max_elem.first;
}