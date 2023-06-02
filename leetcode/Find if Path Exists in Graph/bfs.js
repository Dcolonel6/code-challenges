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

const buildGraph = (edges) => {
    const graph = {};
    for(let edge of edges){
        const [vertixA, vertixB] = edge
        //checks to see if vertix in graph if not its initialize an empty ary
        if(!(vertixA in graph)) graph[vertixA] = []
        if(!(vertixB in graph)) graph[vertixB] = []
        graph[vertixA].push(vertixB)
        graph[vertixB].push(vertixA)
    }

    return graph
};
console.log(validPath(6, [[0,1],[0,2],[3,5],[5,4],[4,3]], 0, 5))
