function treeByLevels (rootNode) {
    if(rootNode === null)	return [];
    let queue = [rootNode]
    let values = []
    while (queue.length > 0){
      let current = queue.shift()
      values = [...values, current.value]
      if( current.left !== null) queue = [...queue, current.left]
      if( current.right !== null) queue = [...queue, current.right]
    }
    return values
  }