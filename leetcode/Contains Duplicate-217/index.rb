# @param {Integer[]} nums
# @return {Boolean}
def contains_duplicate(nums)
    (nums.length - nums.uniq.length) > 0
end