# [Extract the domain name from a URL](https://www.codewars.com/kata/514a024011ea4fb54200004b/train/ruby)
Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:

```
* url = "http://github.com/carbonfive/raygun" -> domain name = "github"
* url = "http://www.zombie-bites.com"         -> domain name = "zombie-bites"
* url = "https://www.cnet.com"                -> domain name = cnet"
```
## Lesson
If you use the method  =~ from the Regexp class, any name used to identify captures will be converted into a variable with the value being the matched string
