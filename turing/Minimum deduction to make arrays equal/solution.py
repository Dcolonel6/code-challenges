from typing import List
from collections import Counter
from itertools import combinations


def solution(arr1 : List[int], arr2: List[int]) -> int:
    arr1.sort()
    arr2.sort()
    n = len(arr2)  # Length of arr2 after removal of 2 elements from arr1

    min_y = float('inf')

    # Try removing all possible pairs in arr1
    for remove_indices in combinations(range(len(arr1)), 2):
        temp_arr = []

        for i in range(len(arr1)):
            if i not in remove_indices:
                temp_arr.append(arr1[i])

        # Compute potential y
        potential_y = []
        for i in range(n):
            potential_y.append(arr2[i] - temp_arr[i])

        # If all y values are the same, it's a valid y
        if len(set(potential_y)) == 1:
            min_y = min(min_y, potential_y[0])

    return min_y if min_y != float('inf') else -1  # Return -1 if no valid y found


if __name__ == "__main__":
    print(solution([5, 30, 25, 20, 15], [22, 18, 28])) # -3
    print(solution([6, 9, 9, 6], [12, 12])) # 3
