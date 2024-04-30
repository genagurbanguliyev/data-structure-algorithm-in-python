def minSteps_test( s: str, t: str) -> int:
    ss: dict = {}
    tt: dict = {}

    for letter in s:
        ss[letter] = ss.get(letter, 0) + 1

    for letter in t:
        tt[letter] = tt.get(letter, 0) + 1

    result: int = 0
    for letter, count in tt.items():
        result += max(0, count - ss.get(letter, 0))
    return result


# Best Solution
def minSteps(self, s: str, t: str) -> int:
    a = 0

    for i in range(ord('a'), ord('z') + 1):
        v = s.count(chr(i)) - t.count(chr(i))
        a += v if v > 0 else 0
    return a


if __name__ == '__main__':
    print(minSteps("leetcode", "practice"))