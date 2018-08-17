def get_maxSubStr(str1, str2):
    str_all_sub = [str1[i:i + x + 1] for x in range(len(str1)) for i in range(len(str1) - x)]

    str_all_sub.reverse()

    for i in str_all_sub:
        if i in str2:
            return i


print(get_maxSubStr("abcdee", "qwsaabcdeq"))
