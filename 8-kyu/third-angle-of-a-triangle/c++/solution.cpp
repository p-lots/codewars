class Triangle {
public:
  static int otherAngle(int a, int b);
};

int Triangle::otherAngle(int a, int b)
{
    return 180 - (a + b);
}