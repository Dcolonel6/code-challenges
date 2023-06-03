/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    const queue = s.split("")
    const alreadyVisited = new Set()
    //let longest = ""

    while(queue.length){
        const current = queue.shift()
        if(!alreadyVisited.has(current)){
            alreadyVisited.add(current)
        }
        else {
            return Array.from(alreadyVisited).join('')
        }
    }
   return Array.from(alreadyVisited).join('') 
};

console.log(lengthOfLongestSubstring("abcabcbb"))