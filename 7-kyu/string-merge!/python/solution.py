def string_merge(string1, string2, letter):
    str1_idx = string1.find(letter)
    str2_idx = string2.find(letter)
    return string1[:str1_idx] + string2[str2_idx:]