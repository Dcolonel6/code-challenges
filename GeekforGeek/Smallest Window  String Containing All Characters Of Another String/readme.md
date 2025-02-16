# [Smallest window containing all characters of another string](https://www.geeksforgeeks.org/problems/smallest-window-in-a-string-containing-all-the-characters-of-another-string-1587115621/1)
***

Given two strings **s1** and **s2**. Find the smallest window in the string **s1** 
consisting of all the characters(**including duplicates**) of the string **s2**. 
Return "" in case no such window is present. 
If there are multiple such windows of the same length, 
return the one with the **least starting index.**
Note: All characters are in lowercase letters. 
# Examples:
```
**Input:** s1 = "timetopractice", s2 = "toc"  
**Output:** "toprac"  
**Explanation:** "toprac" is the smallest substring in which "toc" can be found.  
```
```
**Input:** s1 = "zoomlazapzo", s2 = "oza"  
**Output:** "apzo"  
**Explanation:** "apzo" is the smallest substring in which "oza" can be found.  
```
``` 
**Input:** s1 = "zoom", s2 = "zooe"  
**Output:** ""  
**Explanation:** No window is present containing all characters of s2.  
```

# Constraints: 
- 1 ≤ |s1|, |s2| ≤ 105
- s1,s2 consists of lowercase letters only