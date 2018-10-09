import turtle


t = turtle.Pen()
ts = t.getscreen()
ts.bgcolor("black")
a = 0
t.speed('fast')
for i in range(a, 100):
	t.color( "pink" )
	t.forward( a )
	t.right( 170 )
	a = a+1
t.up()
t.left(180)
t.forward(100)
t.down()
b = 0
for i in range(b, 180):
	t.color( "red" )
	t.forward(b)
	t.right(163)
	b = b+1
t.up()
t.right(90)
t.forward(200)
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
t.up()
t.right(180)
t.forward(500)
t.down()
e = 0
for i in range(e, 150):
	t.color( "skyblue" )
	t.forward(e)
	t.left(175)
	e = e+1
t.up()
t.right(120)
t.forward(200)
t.down()
f = 0
for i in range(f, 160):
	t.color( "blue" )
	t.forward(f)
	t.left(167)
	f = f+1
t.up()
t.forward(400)
t.down()
g = 0
for i in range(g, 200):
	t.color( "yellow" )
	t.forward(g)
	t.left(159)
	g = g + 1
t.up()
t.left(120)
t.forward(600)
t.down()
turtle.exitonclick()