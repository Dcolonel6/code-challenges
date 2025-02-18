# [First character that repeats](https://www.codewars.com/kata/54f9f4d7c41722304e000bbb/train/python)

Find the first character that repeats in a String and return that character.

```
first_dup('tweet') => 't'
first_dup('like') => None
```

_This is not the same as finding the character that repeats first. In that case, an input of 'tweet' would yield 'e'._

Another example:

In `'translator'` you should return `'t'`, not `'a'`.
```
v      v  
translator
  ^   ^
```
While second `'a'` appears before second `'t'`, the first `'t'` is before the first `'a'`.
