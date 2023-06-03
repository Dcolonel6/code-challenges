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
module.exports = bfs