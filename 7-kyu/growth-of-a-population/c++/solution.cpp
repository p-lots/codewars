class Arge
{
  public:
  static int nbYear(int p0, double percent, int aug, int p)
  {
      percent /= 100.0;
      int years = 0;
      while (p0 < p) {
          p0 += p0 * percent + aug;
          years++;
      }
      return years;
  }
};