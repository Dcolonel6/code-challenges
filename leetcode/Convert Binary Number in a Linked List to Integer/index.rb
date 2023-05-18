# Definition for singly-linked list.
# class ListNode
#     attr_accessor :val, :next
#     def initialize(val = 0, _next = nil)
#         @val = val
#         @next = _next
#     end
# end
# @param {ListNode} head
# @return {Integer}
def get_decimal_value(head)
    str = ''
    current_node = head
    while(current_node)
        str += current_node.val.to_s
        current_node = current_node.next
    end
    str.to_i(2)
    
end