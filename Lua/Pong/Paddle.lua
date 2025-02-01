Paddle = Class{}

--initalize our paddle or create instruction for the paddle
--def __init__(self,arguments):
function Paddle:init(x,y,width,height)
    self.x = x
    self.y = y
    --this.whatever = whatever
    self.width = width
    self.height = height
    self.dy = 0
end

--update function that tells the ball what to do 
function Paddle:update(dt)
    if self.dy<0 then
        self.y = math.max(0,self.y+self.dy*dt)
    else
        self.y = math.min(VIRTUAL_HEIGHT-self.height,self.y+self.dy*dt)
    end
end

--render the ball to the screen
function Paddle:render()
    love.graphics.rectangle('fill',self.x,self.y,self.width,self.height)
end