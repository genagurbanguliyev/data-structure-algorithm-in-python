from typing import List
def reverse_words(s: str) -> str:
    ss: List = s.split()
    start_index: int = 0
    end_index: int = len(ss) - 1
    while start_index < end_index:
        ss[start_index], ss[end_index] = ss[end_index], ss[start_index]
        start_index += 1
        end_index -= 1
    return ' '.join(ss)

if __name__ == '__main__':
    print(reverse_words('hello world'))