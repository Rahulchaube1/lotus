import turtle

# Setup the screen
screen = turtle.Screen()
screen.bgcolor("lightblue")  # Set a nice background color for the sky

# Create the turtle object
pen = turtle.Turtle()
pen.shape("turtle")
pen.speed(10)
pen.width(2)

# Function to draw a lotus petal
def draw_petal(color, radius):
    pen.color(color)
    pen.begin_fill()
    pen.circle(radius, 60)  # Draw a half-circle (60 degrees)
    pen.left(120)
    pen.circle(radius, 60)  # Draw the other half of the circle (60 degrees)
    pen.left(120)
    pen.end_fill()

# Function to draw a lotus flower with multiple colorful petals
def draw_lotus(x, y):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    colors = ["pink", "purple", "white", "lightpink", "lavender", "peach"]
    for i in range(6):  # Draw 6 petals
        pen.setheading(i * 60)  # Rotate the turtle for each petal
        draw_petal(colors[i], 100)

# Function to draw a lotus leaf
def draw_leaf(x, y):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.color("forest green")
    pen.begin_fill()
    pen.circle(50, 180)  # Create a semi-circle leaf shape
    pen.end_fill()

# Function to draw a water lily (small version of lotus flower)
def draw_water_lily(x, y):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    colors = ["yellow", "white", "lightblue"]
    for i in range(6):  # Draw 6 petals
        pen.setheading(i * 60)
        draw_petal(colors[i % 3], 60)

# Function to draw jasmine blossoms (small round shapes)
def draw_jasmine(x, y):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.color("white")
    for i in range(5):
        pen.begin_fill()
        pen.circle(20)
        pen.end_fill()
        pen.penup()
        pen.forward(30)
        pen.pendown()

# Function to draw a simple iris flower
def draw_iris(x, y):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    colors = ["blue", "purple", "yellow"]
    for i in range(6):  # Draw 6 petals in a rotated manner
        pen.setheading(i * 60)
        draw_petal(colors[i % 3], 60)

# Function to draw the pond water
def draw_water():
    pen.penup()
    pen.goto(-200, -200)
    pen.pendown()
    pen.color("lightblue")
    pen.begin_fill()
    pen.circle(250)
    pen.end_fill()

# Function to draw droplets on leaves (optional)
def draw_droplets(x, y):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.color("lightblue")
    for _ in range(5):  # Create 5 droplets on the leaf
        pen.begin_fill()
        pen.circle(5)
        pen.end_fill()
        pen.penup()
        pen.forward(15)
        pen.pendown()

# Start drawing the scene
pen.hideturtle()

# Draw the pond
draw_water()

# Draw multiple lotus flowers at different positions
draw_lotus(0, 50)  # Centered lotus
draw_lotus(-150, 100)  # Off-center lotus
draw_lotus(150, 150)  # Another lotus

# Draw leaves under the lotus flowers
draw_leaf(-30, -20)  # Leaves for first lotus
draw_leaf(100, -50)  # Leaves for second lotus
draw_leaf(-100, -100)  # Leaves for third lotus

# Draw additional water lilies around the pond
draw_water_lily(-200, -100)
draw_water_lily(200, -150)
draw_water_lily(-50, -250)

# Draw jasmine blossoms near the edges of the pond
draw_jasmine(-180, -180)
draw_jasmine(180, -230)

# Draw iris flowers around the pond's edge
draw_iris(-250, -50)
draw_iris(250, -100)

# Draw droplets on the leaves for more realism
draw_droplets(-30, 30)
draw_droplets(100, -20)
draw_droplets(-100, -40)

# Keep the window open until clicked
screen.exitonclick()
