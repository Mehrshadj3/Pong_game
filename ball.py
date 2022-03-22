from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.shapesize(stretch_wid= 1, stretch_len= 1)
        self.penup()
        self.x = 10
        self.y = 10
        self.ball_speed = 0.1

    def move(self):
        x_pos = self.xcor() + self.x
        y_pos = self.ycor() + self.y
        self.goto(x_pos, y_pos)


    def bounce_y(self):
        self.y *= -1


    def bounce_x(self):
        self.x *= -1
        self.ball_speed *= 0.9


    def reset_ball(self):
        self.goto(0,0)
        self.bounce_x()
        self.ball_speed = 0.1