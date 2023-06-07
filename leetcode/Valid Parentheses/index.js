/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {   
    const stack = [];
    const aryCharacters = s.split("");    
    
    for (const character of aryCharacters) {
        if (character === "(" || character === "{" || character === "[") {
        stack.unshift(character);
        } else if (character === ")" && stack[0] === "(") {
            stack.shift();      
        } else if (character === "}" && stack[0] === "{") {
            stack.shift();
        } else if (character === "]" && stack[0] === "[") {
            stack.shift();
        }else{
            return false;  
        } 
    }  
    return stack.length <= 0;
};

const possibilitiesOfS = ["()", "()[]{}", "(]", "[", "((" ];
possibilitiesOfS.forEach((possible) => {
  console.log(`${possible} =>`, isValid(possible));
});
