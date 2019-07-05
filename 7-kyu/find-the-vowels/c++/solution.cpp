#include <cctype>

bool isVowel(char c)
{
  if (!std::isalpha(c)) return false;
  c = std::tolower(c);
  return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' || c == 'y';
}

std::vector<int> vowelIndices(std::string word)
{
  std::vector<int> res;
  for (unsigned i = 0; i < word.length(); i++) {
    if (isVowel(word[i])) res.push_back(i + 1);
  }
	return res;
}