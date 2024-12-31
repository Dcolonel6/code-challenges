from typing import List

"""
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, 
and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
Merge nums1 and nums2 into a single array sorted in non-decreasing order.
The final sorted array should not be returned by the function, but instead be stored inside the array nums1.
To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that 
should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
"""


class MergeSorted:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # m is length of array num1 and n is length of array nums2
        merged_ary = []

        index_num1 = 0
        index_num2 = 0

        while index_num1 < m and index_num2 < n:
            num1 = nums1[index_num1]
            num2 = nums2[index_num2]

            if num1 == num2:
                merged_ary.append(num1)
                merged_ary.append(num2)
                index_num1 += 1
                index_num2 += 1
            elif num1 < num2:
                merged_ary.append(num1)
                index_num1 += 1
            else:
                merged_ary.append(num2)
                index_num2 += 1

        # check if arrays indices are the same as the lengths m, n
        if index_num2 < n:
            # we left some elements on nums2
            leftovers_nums2 = nums2[index_num2:n]
            merged_ary.extend(leftovers_nums2)
        if index_num1 < m:
            # we left some elements on nums1
            leftovers_nums1 = nums1[index_num1:m]
            merged_ary.extend(leftovers_nums1)

        return merged_ary


if __name__ == "__main__":
    # print(MergeSorted().merge([1,2,3,0,0,0], 3, [2,5,6], 3))
    print(MergeSorted().merge([0],0,[1], 1 ))



