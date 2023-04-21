function bouncingBall(h, bounce, window){
    // Qualify the condition that must be met
    const cond = h > 0 && bounce > 0 && bounce < 1 && window < h;
    // Check the condition
    if (cond) {
      // If condition is met, the ball will be seen once going up...
      // And once coming down, as well as the first time its dropped
      return h < window ? -1 : 2 + bouncingBall(h * bounce, bounce, window);
    } else {
      // If condition is not met, per instructions, return -1
      return -1;
    }
  }
  
  console.log(bouncingBall(3, 0.66, 1.5))