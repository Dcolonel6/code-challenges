# [Simple Encryption #1 - Alternating Split](https://www.codewars.com/kata/57814d79a56c88e3e0000786/train/ruby)

Implement a pseudo-encryption algorithm which given a string S and an integer N concatenates all the odd-indexed characters of S with all the even-indexed characters of <code>S</code>, this process should be repeated N times.

## Examples:
```
encrypt("012345", 1)  =>  "135024"
encrypt("012345", 2)  =>  "135024"  ->  "304152"
encrypt("012345", 3)  =>  "135024"  ->  "304152"  ->  "012345"

encrypt("01234", 1)  =>  "13024"
encrypt("01234", 2)  =>  "13024"  ->  "32104"
encrypt("01234", 3)  =>  "13024"  ->  "32104"  ->  "20314"
```

Together with the encryption function, you should also implement a decryption function which reverses the process.

If the string <code>S</code> is an empty value or the integer N is not positive, return the first argument without changes.