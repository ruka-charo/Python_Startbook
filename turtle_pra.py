import turtle

kame = turtle.Turtle()
kame.shape('turtle')

#%%正三角形 (for文)
for i in range(3):
    kame.fd(200)
    kame.left(120)

#%%星形
for i in range(5):
    kame.fd(200)
    kame.left(144)

#%%原点中心の円軌道の関数化
def circle_w(target,r):
    target.penup()
    target.fd(r)
    target.left(90)
    target.pendown()
    target.circle(r)
    target.penup()
    target.home()
    target.pendown()

#%%四角螺旋構造
def spiral_rac(target,k=0,l=20,f=300):
    while target.distance(0,0) < f:
        target.fd(l + k)
        target.right(90)
        k += l

#%%ランダム移動
import random

while kame.distance(0,0) < 100:
    kame.left(random.randint(1,360))
    kame.fd(15)

#%%ランダム移動（永遠に）
import random

while kame.distance(0,0) < 100:
    kame.left(random.randint(1,360))
    kame.fd(15)
    if kame.distance(0,0) >= 100:
        kame.undo()
