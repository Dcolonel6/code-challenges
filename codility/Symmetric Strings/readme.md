A string made of even number of characters ( `<` and/or `>`) is called symmetric if all characters in its first half are `<` and all characters in its second half are `>`. Examples of symmetric strings are `""`(empty string), `<>`, `<<>>`, `<<<>>>` etc.

Write a function:
` function solution(s);`
that, given a string S made of N characters (`<`, `>` and/or `?`), returns the length of the longest symmetric substring that can be obtained after replacing question marks with `<` or `>` characters

## Examples:
* For `S = <><??>> `, after replacing all question marks with `<` and the string `<><<<>>` is obtained. Its longest symmetric substring is `<<>>`, so the function should return 4.

* For `S = ??????`, the optimal option is to replace the first three question marks with `<` and the next three question marks with `>`, thus obtaining the string `<<<>>>`. The function should return 6.

* For `S = <<?`, the function should return 2.

Write an efficient algorithm for the following assumptions:
    * the length of string S is within the range [1...200,000]
    * string S is made only of the following characters: `<`, `>` and/or `?`