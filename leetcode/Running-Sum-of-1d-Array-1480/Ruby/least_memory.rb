# @param {Integer[]} nums
# @return {Integer[]}
#uses the least memory when it scales...according leetcode, its 210.8MB
def running_sum(nums)
    nums.each_with_index.map do |num, index|
      if index == 0
        num
      else
        nums[0..index].sum
      end
    end
  end