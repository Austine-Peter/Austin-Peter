def is_anagram2(str1, str2):
    list1 = list(str1)
    list2 = list(str2)
    list1.sort()
    list2.sort()
    return (list1 == list2)

print(is_anagram2("listen","silent"))