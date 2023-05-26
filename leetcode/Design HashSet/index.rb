class MyHashSet
    def initialize()
        @ary = []        
    end


=begin
    :type key: Integer
    :rtype: Void
=end
    def add(key)
       @ary << key 
    end


=begin
    :type key: Integer
    :rtype: Void
=end
    def remove(key)
        @ary.include? key if @ary.delete(key)            
    end


=begin
    :type key: Integer
    :rtype: Boolean
=end
    def contains(key)
        @ary.include? key
    end


end

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet.new()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)