std::string get_middle(std::string input) 
{
  return input.length() % 2 == 0
      ? input.substr(input.length() / 2 - 1, 2)
      : input.substr(input.length() / 2, 1);
}