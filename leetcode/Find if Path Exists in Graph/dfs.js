const {buildGraph} = require("./graph");

var validPath = function(n, edges, source, destination) {
    const graph = buildGraph(edges); 
    const alreadyChecked = new Set()  
    return hasPath(graph, source, destination, alreadyChecked);
};

const hasPath = (grph, src, dest, alreadyChecked) => {    
    if(src === dest) return true;
    if(!alreadyChecked.has(src)){
        alreadyChecked.add(src)
        for(let neighbour of grph[src]){
            
            if(hasPath(grph, neighbour, dest, alreadyChecked)) return true
        }
    }
    return false;
}
console.log(validPath(6, [[0,1],[0,2],[3,5],[5,4],[4,3]], 0, 5))