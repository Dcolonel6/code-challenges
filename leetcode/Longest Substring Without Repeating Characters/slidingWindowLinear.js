// solution has a O(n) time complexity
var lengthOfLongestSubstring = function(s) {  
    let leftPointer = 0, max = 0
    const tracker = {}
    if(s.length <= 2) return s.length
    

    for(let rghtPointer = 0; rghtPointer < s.length; rghtPointer++){
        const char = s[rghtPointer]                
        if(Object.hasOwn(tracker, char) && tracker[char] >= leftPointer){
            leftPointer = tracker[char] + 1
        }
        tracker[char] = rghtPointer                         
        max = Math.max(max, rghtPointer - leftPointer + 1)
    }
    return max

}


console.log(lengthOfLongestSubstring("abcabcbb"))
console.log(lengthOfLongestSubstring("bbbbb"))
console.log(lengthOfLongestSubstring("pwwkew"))
console.log(lengthOfLongestSubstring("abcdefgh"))
console.log(lengthOfLongestSubstring(""))
console.log(lengthOfLongestSubstring("nfpdmpi"))