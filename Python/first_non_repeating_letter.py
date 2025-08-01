def first_non_repeating_letter(string):
    string_copy = string.lower()
    for i in range(len(string)) :
        if (string_copy.count(string_copy[i]) == 1) :
            return string[i]
    return ""
