/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {   
    const stack = [];
    const aryCharacters = s.split("");    
    
    for (const character of aryCharacters) {
        if (character === "(" || character === "{" || character === "[") {
        stack.push(character);
        } else if (character === ")" && stack[stack.length -1] === "(") {
            stack.pop();      
        } else if (character === "}" && stack[stack.length -1] === "{") {
            stack.pop();
        } else if (character === "]" && stack[stack.length -1] === "[") {
            stack.pop();
        }else{
            return false;  
        } 
    }  
    return stack.length <= 0;
};

const possibilitiesOfS = ["()", "{[]}", "()[]{}", "(]", "[", "((" ];
possibilitiesOfS.forEach((possible) => {
  console.log(`${possible} =>`, isValid(possible));
});
