import turtle
t = turtle.Pen()
a = 0
t.speed('fast')
for i in range(a, 100):
	t.color( "pink" )
	t.forward
	t.circle( a)
	a = a+1
t.up()
t.left(180)
t.forward(100)
t.down()
b = 0
for i in range(b, 180):
	t.color( "red" )
	t.forward(b)
	t.right(160)
	b = b+1
t.up()
t.right(180)
t.forward(100)
t.down()
c =0
for i in range(c, 150):
	t.color( "purple" )
	t.forward(c)
	t.left(150)
	c = c+1
t.up()
t.left(30)
t.forward(300)
t.down()
d = 0
for i in range(d, 150):
	t.color( "green" )
	t.forward(d)
	t.left(140)
	d = d+1





turtle.exitonclick()