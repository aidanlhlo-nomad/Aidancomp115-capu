import turtle

# 1. Setup screen
wn = turtle.Screen()
wn.bgcolor("lightblue")
wn.title("Cartoon Bird")

# 2. Create turtle
pic = turtle.Turtle()
pic.speed(5)
pic.pensize(2)

# Body proportions
body_x = 0
body_y = -80

# ---------------------------
# 3. Draw body
pic.penup()
pic.goto(body_x, body_y)
pic.color("yellow")
pic.pendown()

pic.begin_fill()
pic.circle(80)
pic.end_fill()

# ---------------------------
# 4. Draw wings
pic.penup()
pic.goto(body_x-68,body_y+115)
pic.color("yellow")
pic.setheading(0)
pic.pendown()
pic.begin_fill
pic.circle(-30,90)
pic.circle(-60, 90)
pic.circle(-30, 90)
pic.circle(-60, 90)
pic.end_fill()

pic.penup()
pic.goto(body_x+75, body_y+40)
pic.color("yellow")
pic.setheading(0)
pic.pendown()
pic.begin_fill
pic.circle(30,90)
pic.circle(60, 90)
pic.circle(30, 90)
pic.circle(60, 90)
pic.end_fill


# ---------------------------
# 5. Draw head
pic.penup()
pic.goto(body_x, body_y + 120)
pic.pendown()

pic.begin_fill()
pic.circle(40)
pic.end_fill()

# ---------------------------
# 6. Draw beak
pic.penup()
pic.goto(body_x+1, body_y + 130)
pic.color("orange")
pic.setheading(0)
pic.pendown()

pic.begin_fill()
pic.forward(25)
pic.left(120)
pic.forward(20)
pic.left(120)
pic.forward(20)
pic.end_fill()

# ---------------------------
# 7. Draw eyes
pic.penup()
pic.goto(body_x, body_y + 155)
pic.color("black")
pic.pendown()
pic.begin_fill()
pic.circle(7)
pic.end_fill()

pic.penup()
pic.goto(body_x + 20, body_y + 155)
pic.pendown()
pic.begin_fill()
pic.circle(7)
pic.end_fill()

# ---------------------------
# 8. Draw feet
pic.penup()
pic.goto(body_x - 25, body_y - 1)
pic.color("yellow")
pic.setheading(-90)
pic.pendown()

pic.forward(40)
pic.right(30)
pic.forward(20)
pic.backward(20)
pic.left(60)
pic.forward(20)

pic.penup()
pic.goto(body_x + 25, body_y - 1)
pic.setheading(-90)
pic.pendown()

pic.forward(40)
pic.right(30)
pic.forward(20)
pic.backward(20)
pic.left(60)
pic.forward(20)

# ---------------------------
pic.hideturtle()
turtle.done()


