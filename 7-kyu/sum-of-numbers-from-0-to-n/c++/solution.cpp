using namespace std;

class SequenceSum{
  int count;
  public:
  SequenceSum (int);
  string showSequence(){
      if (count < 0) return std::string(std::to_string(count) + "<0");
      else if (count == 0) return "0=0";
      string ret = "0";
      int sum = 0;
      for (unsigned i = 1; i <= count; i++) {
          ret += "+" + std::to_string(i);
          sum += i;
      }
      ret += " = ";
      ret += std::to_string(sum);
      return ret;
  }
};

SequenceSum::SequenceSum (int c) {
  count = c;
}