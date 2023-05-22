# [Find A String](https://www.hackerrank.com/challenges/find-a-string/problem?isFullScreen=true)

In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left.

**NOTE:** String letters are case-sensitive.

## Input Format

The first line of input contains the original string. The next line contains the substring.

## Constraints
<code> 1 <= len(string) <= 200</code>

Each character in the string is an ascii character.

## Output Format

Output the integer number indicating the total number of occurrences of the substring in the original string.

## Sample Input
```
ABCDCDC
CDC
Sample Output
```
```
2
```
## Concept

Some string processing examples, [such as these](https://www.thelearningpoint.net/computer-science/learning-python-programming-and-data-structures/learning-python-programming-and-data-structures--tutorial-12--string-manipulation), might be useful.
There are a couple of new concepts:
In Python, the length of a string is found by the function <code>len(s)</code>, where *S* is the string.
To traverse through the length of a string, use a for loop:
<br>
<code>
for i in range(0, len(s)):
    print (s[i])
</code>    

A range function is used to loop over some length:

<code>
    range (0, 5)
</code>
Here, the range loops over 0 to 4.5 is excluded.

## What have i learnt?

This is a problem testing on sliding window technique