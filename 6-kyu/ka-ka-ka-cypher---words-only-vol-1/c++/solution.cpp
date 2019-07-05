#include <cctype>

bool is_vowel(char c)
{
    c = tolower(c);
    return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
}

string kaCokadekaMe(string word)
{
     for (unsigned i = 0; i < word.length(); i++) {
        // "ka" goes after vowel
        if (is_vowel(word[i])) {
            // when there are multiple vowels, "ka" goes after the last vowel
            while (is_vowel(word[i])) {
                i++;
            }
            if (i < word.length()) {
                word.insert(i, "ka");
                i += 2;
            }
        }
    }
    // word starts with "ka"
    word = "ka" + word;
    return word;
}