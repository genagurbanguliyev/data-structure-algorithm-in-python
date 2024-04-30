def is_anagram_test(str1: str, str2: str) -> bool:
    if len(str1) != len(str2):
        return False

    str1 = sorted(str1)
    str2 = sorted(str2)

    for i in range(len(str1)):
        if str1[i] != str2[i]:
            return False
    return True

# Best solution
def is_anagram(str1: str, str2: str) -> bool:
    from collections import Counter
    return Counter(str1) == Counter(str2)



if __name__ == '__main__':
    str1 = 'restful'
    str2 = 'fluster'
    print(is_anagram(str1, str2))