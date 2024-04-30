from typing import List


def dutch_national_flag(arr: List[int], midd: int) -> None:
    i, j = 0, 0;
    k = len(arr) - 1;
    while j < k:
        if arr[j] < midd:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j += 1
        elif arr[j] > midd:
            arr[j], arr[k] = arr[k], arr[j]
            k -= 1
        else:
            j += 1


import time
if __name__ == '__main__':
    start_time = time.time()
    a = [0,1,1,0,2,1,2,0]
    dutch_national_flag(arr=a, midd=1)
    print(a)
    end_time = time.time()
    print("Time taken:", end_time - start_time, "seconds")