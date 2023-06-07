# [20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses/description/)

Given a string s containing just the characters <code>'(', ')', '{', '}', '[' and ']'</code>, determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

## Example 1:
```
Input: s = "()"
Output: true
```
## Example 2:
```
Input: s = "()[]{}"
Output: true
```
## Example 3:
```
Input: s = "(]"
Output: false
``` 

## Constraints:

- <code>1 <= s.length <= 104</code>
- <code>s</code> consists of parentheses only <code>'()[]{}'</code>.