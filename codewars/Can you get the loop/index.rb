def loop_size(node)
    ary = []  
    current_node = node
    count = 0
    while(current_node)
      if(ary.include? current_node.object_id)
        ary.push(current_node.object_id)
        break
      end
      ary.push(current_node.object_id)
      count += 1
      current_node = current_node.next
    end
    last_id = ary.last
    id_head_circular = ary.find_index(last_id)
    count - id_head_circular
  end