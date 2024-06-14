def remove_consecutive_duplicates(s):
    i = 0
    while i < len(s) - 1:
        if s[i] == s[i + 1]:
            del s[i]
        else:
            i += 1
    return s
print(remove_consecutive_duplicates(list('aaabbbccc')))