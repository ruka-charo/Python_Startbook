import turtle

class Kame(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')

    def draw_bar(self,height,width = 40):
        self.left(90)
        self.fd(height)
        self.right(90)
        self.fd(width)
        self.right(90)
        self.fd(height)
        self.left(90)

    def histogram(self,data,x_0 = -200,y_0 = -150):
        self.penup()
        self.goto(x_0,y_0)
        self.pendown()
        for i in range(10):
            self.draw_bar(data[i])
        self.goto(x_0,y_0)
