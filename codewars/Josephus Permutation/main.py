def traverse(node, k, number_of_items):
    current = node
    index = 1
    permutations = list()

    while True:
        next_node = current.next
        prev_node = current.prev
        if index % k == 0:
            value = current.val
            # append the value to perm list
            permutations.append(value)

            # remove the current  node
            prev_node.next = next_node
            next_node.prev = prev_node
            current.next = None
            current.prev = None
        # update current node to incoming node
        current = next_node

        if number_of_items == len(permutations):
            break
        index += 1
    return permutations


