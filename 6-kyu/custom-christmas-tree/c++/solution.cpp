std::string customChristmasTree(const std::string& chars, int n){
  int num_before_spaces = n - 1, chars_it = 0, num_chars_per_line = 1;
  std::string ret = "";
  for (unsigned i = 1; i <= n; i++) {
    if (num_before_spaces > 0) ret += std::string(num_before_spaces, ' ');
    for (unsigned j = 0; j < num_chars_per_line; j++) {
      ret += chars[chars_it++];
      if (chars_it >= chars.length()) chars_it = 0;
      if (j < num_chars_per_line - 1) ret += " ";
    }
    num_before_spaces--;
    num_chars_per_line++;
    ret += "\n";
  }
  for (unsigned i = 0; i < n / 3; i++) {
    ret += std::string((2 * n - 1) / 2, ' ') + "|\n";
  }
  ret.pop_back();
  return ret;
}