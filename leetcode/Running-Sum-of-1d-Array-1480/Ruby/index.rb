# @param {Integer[]} nums
# @return {Integer[]}
#performance time: 90ms, memory 211MB
def running_sum(nums)
    nums.each_with_object([]) {|ele,obj| obj << obj.fetch(-1, 0) + ele}
end