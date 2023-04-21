# sightings = 2 * number of bounces > window - 1
def bouncingBall(h, bounce, window)
    # your code  
  return -1 unless h > 0 && bounce.between?(0,1) && window < h
  height_after_bounce = h
  count_bounces = 0
  until height_after_bounce < window
    count_bounces += 1
    height_after_bounce = height_after_bounce * bounce    
    #binding.pry
  end  
  count_bounces * 2 - 1
end

def print_bounce h, bounce, window
  puts "Number of bounces: #{bouncingBall(h, bounce, window)}"
end
