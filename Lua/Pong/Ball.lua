Ball = Class{}

--initalize our ball or create instruction for the balls
--def __init__(self,arguments):
function Ball:init(x,y,width,height)
    self.x = x
    self.y = y
    --this.whatever = whatever
    self.width = width
    self.height = height

    --along with the defualt info, we need the velocity variables dx and dy
    self.dx = math.random(2) == 1 and 100 or -100
    self.dy = math.random(-50,50)
end

--reset function to move it back to the middle
function Ball:reset()
    self.x = VIRTUAL_WIDTH / 2 -2
    self.y = VIRTUAL_HEIGHT / 2 -2
    self.dx = math.random(2) == 1 and 100 or -100
    self.dy = math.random(-50,50)
end

function Ball:collides(paddle)
    --checking to see if i colliding with the walls
    if self.y > (paddle.y +paddle.height) or paddle.y > self.y + self.height then
        return false
    end
    --checking to see if i colliding with the paddles
    if self.x > (paddle.x +paddle.width) or paddle.x > (self.x + self.height) then
        return false
    end
    return true
end

--update function that tells the ball what to do 
function Ball:update(dt)
    self.x = self.x + self.dx * dt
    self.y = self.y + self.dy * dt
end

--render the ball to the screen
function Ball:render()
    love.graphics.rectangle('fill',self.x,self.y,self.width,self.height)
end

