import turtle as t

t.penup()
t.setpos(0,-30)
t.pendown()

t.pensize(10)
t.color("pink")


def curve():
    for i in range(200):
        t.right(1)
        t.forward(1)

t.fillcolor('pink')
t.begin_fill()

t.left(140)
t.forward(111.65)

curve()
t.left(120)

curve()
t.forward(111.65)
t.end_fill()

t.ht()
t.done()
