/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {    
    let count = 0
    let str = s.slice(count)
    while(str.length){             
        const subString = bfs(str)        
        if(s.includes(subString)) return subString.length
        count++
        str = s.slice(count)
    }
};

const bfs = (s) => {
    const queue = s.split("")
    const alreadyVisited = new Set()
    while(queue.length){
        const current = queue.shift()
        if(!alreadyVisited.has(current)){
            alreadyVisited.add(current)
        }  
    }
   return Array.from(alreadyVisited).join('')
}

console.log(lengthOfLongestSubstring("abcabcbb"))
console.log(lengthOfLongestSubstring("bbbbb"))
console.log(lengthOfLongestSubstring("pwwkew"))
console.log(lengthOfLongestSubstring("abcdefgh"))