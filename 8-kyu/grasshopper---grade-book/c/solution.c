char get_grade(int a, int b, int c)
{
    int avg = (a + b + c) / 3;
    if (avg < 60) return 'F';
    else if (avg < 70) return 'D';
    else if (avg < 80) return 'C';
    else if (avg < 90) return 'B';
    else return 'A';
}