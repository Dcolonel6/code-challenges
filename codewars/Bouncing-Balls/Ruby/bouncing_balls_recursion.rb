def bouncingBall(h, bounce, window)
    cond =  h > 0 && bounce.between?(0,1) && window < h
    if(cond)
        return  h < window ? -1 : 2 + bouncingBall(h * bounce, bounce, window)
    else
        return -1
    end
end

puts bouncingBall(3, 0.66, 1.5)