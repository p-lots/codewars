class Person
{
  public:
    Person(int age) : m_age(age) {}
  
    bool operator==(const Person& other) const
    {
      return this->m_age == other.m_age;
    }
    
    bool operator!=(const Person& other) const
    {
      return !(*this == other);
    }
    
    bool operator<=(const Person& other) const
    {
      return this->m_age <= other.m_age;
    }
    
    bool operator>=(const Person& other) const
    {
      return this->m_age >= other.m_age;
    }
    
    bool operator<(const Person& other) const
    {
      return *this <= other && *this != other;
    }
    
    bool operator>(const Person& other) const
    {
      return *this >= other && *this != other;
    }
    
  private:
    const int m_age;
};