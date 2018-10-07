import turtle

t = turtle.Pen()
t.color("pink")
t.speed('fast')
for i in range(1, 41):
	t.forward(300)
	t.left(164)

t.color("green")

turtle.exitonclick()