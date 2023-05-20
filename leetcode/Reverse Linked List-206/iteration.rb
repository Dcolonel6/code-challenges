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
def reverse_list(head)
    return head if head.nil?
    prev_node = head
    prev_prev_node = nil
    current_node = prev_node.next
    while(current_node)
        prev_node.next = prev_prev_node        
        current_node, prev_node, prev_prev_node = current_node.next,current_node, prev_node       
    end
    prev_node.next = prev_prev_node
    prev_node
end