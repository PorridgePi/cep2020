# Program Filename: 24YZHOU524J_Libya.py
# My Full Name: Zhou Yikun
# My Class: 2H

import turtle as t

def rectangle(l,w,color):
  t.color(color)
  t.fillcolor(color)
  t.begin_fill()
  for i in range(2):
    t.forward(l)
    t.right(90)
    t.forward(w)
    t.right(90)
  t.end_fill()


rectangle(180,60,"royalblue")
t.goto(0,-60)
rectangle(180,60,"yellow")
t.up()

t.goto(200,0)
t.down()
rectangle(180,40,"black")
t.goto(200,-40)
rectangle(180,40,"red")
t.goto(200,-80)
rectangle(180,40,"yellow")
