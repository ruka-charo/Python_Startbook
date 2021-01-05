def circle_w(target,r = 100):
    target.penup()
    target.fd(r)
    target.left(90)
    target.pendown()
    target.circle(r)
    target.penup()
    target.home()
    target.pendown()
