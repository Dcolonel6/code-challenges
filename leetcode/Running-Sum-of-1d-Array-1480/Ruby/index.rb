# @param {Integer[]} nums
# @return {Integer[]}
def running_sum(nums)
    nums.each_with_object([]) {|ele,obj| obj << obj.fetch(-1, 0) + ele}
end