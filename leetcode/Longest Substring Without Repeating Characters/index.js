const bfs = require('./bfs')
/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) { 
    if(s.length <= 1) return s.length   
    let count = 0
    let str = s.slice(count)
    while(str.length){             
        const subString = bfs(str)        
        if(s.includes(subString)) return subString.length
        count++
        str = s.slice(count)
    }
};



console.log(lengthOfLongestSubstring("abcabcbb"))
console.log(lengthOfLongestSubstring("bbbbb"))
console.log(lengthOfLongestSubstring("pwwkew"))
console.log(lengthOfLongestSubstring("abcdefgh"))
console.log(lengthOfLongestSubstring(""))