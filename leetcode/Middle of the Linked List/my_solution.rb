# Definition for singly-linked list.
# class ListNode
#     attr_accessor :val, :next
#     def initialize(val = 0, _next = nil)
#         @val = val
#         @next = _next
#     end
# end
# @param {ListNode} head
# @return {ListNode}
def middle_node(head)
    ary_of_nodes = []
    current_node = head
    count = 0
    while(current_node)
        ary_of_nodes.push(current_node)
        current_node = current_node.next
        count += 1        
    end
    index = count.even? ? count / 2 : count / 2    
    ary_of_nodes[index]    
end


#the solution above is not performant.
# uses o(n) for time and o(n) for space