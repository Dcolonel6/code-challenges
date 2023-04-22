# @param {Integer[]} nums
# @return {Integer[]}
#uses the least time when it scales,54ms
def running_sum(nums)
    last = 0
    summed = []
    for n in 0...nums.length
        last += nums[n]
        summed.push(last)
    
    end
    return summed
end