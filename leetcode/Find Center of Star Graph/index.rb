 # @param {number[][]} edges
 # @return {number}


def find_center(edges)
    tally = edges.flatten.tally
    most_freq =  tally.values.max
    tally.filter{|key, value| value == most_freq}.keys[0]
end

edges = [
    [[1,2],[2,3],[4,2]],
    [[1,2],[5,1],[1,3],[1,4]]
]

edges.each do |edge|
    puts "#{find_center edge}"
end