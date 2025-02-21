//using the sliding window approach
//Time complexity O(n2)

var lengthOfLongestSubstring = function(s) {     
    let max = 0, maxSubstring = ""
    if(s.length <= 1) return {max: s.length, subStr: s, str: s}

    for(let i = 0; i < s.length; i++){
        let substr = ""
        for(let j = i; j < s.length;j++){
            const char = s[j]
            if(substr.includes(char)){
                
                break
            }
            substr += char
            max = Math.max(substr.length, max)
        }
        maxSubstring = maxSubstring.length >= substr.length ? maxSubstring : substr
    }
    return {max: max, subStr: maxSubstring, str: s}

}


console.log(lengthOfLongestSubstring("abcabcbb"))
console.log(lengthOfLongestSubstring("bbbbb"))
console.log(lengthOfLongestSubstring("pwwkew"))
console.log(lengthOfLongestSubstring("abcdefgh"))
console.log(lengthOfLongestSubstring(""))
console.log(lengthOfLongestSubstring("nfpdmpi"))