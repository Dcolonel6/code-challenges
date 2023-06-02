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
module.exports = {buildGraph: buildGraph}