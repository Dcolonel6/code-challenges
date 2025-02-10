# [Check if Permutation is Substring](https://www.geeksforgeeks.org/problems/check-if-permutation-is-substring/1)
***
Given two strings txt and pat having lowercase letters, the task is to check if any permutation of pat is a substring of txt.

## Examples:
```
Input: txt = "geeks", pat = "eke"  
Output: true  
Explanation: "eek" is a permutation of "eke" which exists in "geeks".  
```
~~~
Input: txt = "programming", pat = "rain"  
Output: false  
Explanation: No permutation of "rain" exists as a substring in "programming".  
~~~

 ## Constraints:
- 1 ≤ txt.size() ≤ 105
- 1 ≤ pat.size() ≤ txt.size()
- Both the strings consist of lowercase English alphabets.