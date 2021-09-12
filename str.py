def strings(str1, str2):
    if type(str1) != str and type(str2) != str:
        return 0
    elif str1 == str2:
        return 1
    elif str1 != str2 and len(str1) > len(str2):
        return 2
    elif str1 != str2 and str2 == 'learn':
        return 3
    
print(strings('apple', 'apple'))
print(strings('apple', 'app'))
print(strings('apple', 'learn'))
print(strings(2.1, 2))