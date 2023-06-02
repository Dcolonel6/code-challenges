const {buildGraph} = require("./graph");
/**
 * @param {number} n
 * @param {number[][]} edges
 * @param {number} source
 * @param {number} destination
 * @return {boolean}
 */

var validPath = function(n, edges, source, destination) {
    const graph = buildGraph(edges);
    const hasPath = (grph, src, dest) => {
        const queue = [src];
        const alreadyChecked = new Set()
        if(src === dest) return true;
        while(queue.length){
            const current = queue.shift()
            if(alreadyChecked.has(current)) continue
            alreadyChecked.add(current)
            if(current === dest) return true;
            queue.push(...grph[current]);
        }
        return false;
    }
    return hasPath(graph, source, destination);
    
};

const {buildGraph} = require("./graph");
