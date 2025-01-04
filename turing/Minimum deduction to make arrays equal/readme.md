You are provided with two arrays, arr1 and arr2 having integer values. 
From arr1, exactly two elements have been removed, 
and all remaining elements have been either increased or decreased by the same integer value, denoted by y. 

As a result, arr1 becomes identical to arr2. 
Two arrays are considered identical if they contain the same elements with the same frequency. 
Your task is to find the smallest possible integer y that makes the two arrays identical. 

## Example 1:
**Input**: arr1 = _[5, 30, 25, 20, 15]_, arr2 = _[22, 18, 28]_ <br>
**Output**: -3 <br>
**Explanation**: After removing the elements at indices _**[1, 4]**_ and subtracting **3,** arr1 becomes **[22, 18, 28]**

## Example 2:
**Input**: arr1 = _[6, 9, 9, 6]_, arr2 = _[12, 12]_ <br>
**Output**: 3 <br>
**Explanation**: After removing the elements at indices **_[0, 3]_** and adding **3**, arr1 becomes **_[12, 12]_**

## Constraints
* 3 <= arr1.length <= 200
* arr1.length == arr2.length - 2
* 0 ,= arr[i], arr2[i] <= 1000
* The test cases are generated in a way that there is an integer x such that arr1 can 
become equal to arr2 by removing two elements and adding x to each element of nums1.