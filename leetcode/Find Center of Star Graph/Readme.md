# [Find Center of Star Graph](https://leetcode.com/problems/find-center-of-star-graph/)

There is an undirected **star** graph consisting of <code>n</code> nodes labeled from <code> 1 </code> to <code>n</code>. A star graph is a graph where there is one **center** node and **exactly** <code> n - 1</code> edges that connect the center node with every other node.

You are given a 2D integer array <code>edges</code> where each <code> edges[i] = [ui, vi] </code> indicates that there is an edge between the nodes <code> ui </code> and <code> vi </code>. Return the center of the given star graph.

<img src="" alt="star graph" >

## Example 1:

```
Input: edges = [[1,2],[2,3],[4,2]]
Output: 2
Explanation: As shown in the figure above, node 2 is connected to every other node, so 2 is the center.
```
## Example 2:
```
Input: edges = [[1,2],[5,1],[1,3],[1,4]]
Output: 1
```

## Constraints:

- <code> 3 <= n <= 105 </code>
- <code> edges.length == n - 1 </code>
- <code> edges[i].length == 2 </code>
- <code> 1 <= ui, vi <= n </code>
- <code >ui != vi </code>
- The given <code> edges </code> represent a valid star graph.