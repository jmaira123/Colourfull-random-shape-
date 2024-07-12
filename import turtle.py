import turtle
import random
import math

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")  # Black background

# Create turtle for drawing
artist = turtle.Turtle()
artist.speed(0)  # Fastest speed
artist.width(2)

# List to store shape positions and sizes
shapes = []

# Function to draw a random colored shape
def draw_shape():
    colors = ["#ff6666", "#66ff66", "#6666ff", "#ffa366", "#66ffff", "#ff66ff", "#ffff66", "#ff66a3", "#66a3ff", "#a366ff"]
    color = random.choice(colors)
    shape = random.choice(["circle", "square", "triangle", "star"])

    while True:
        x = random.randint(-300, 300)
        y = random.randint(-200, 200)
        size = random.randint(20, 80)
        
        # Check for overlapping with existing shapes
        overlapping = False
        for sx, sy, ssize in shapes:
            distance = math.sqrt((x - sx)**2 + (y - sy)**2)
            if distance < (size + ssize):
                overlapping = True
                break
        
        if not overlapping:
            break

    shapes.append((x, y, size))

    artist.penup()
    artist.goto(x, y)
    artist.pendown()

    artist.color(color)
    artist.begin_fill()

    if shape == "circle":
        artist.circle(size // 2)
    elif shape == "square":
        for _ in range(4):
            artist.forward(size)
            artist.right(90)
    elif shape == "triangle":
        for _ in range(3):
            artist.forward(size)
            artist.left(120)
    elif shape == "star":
        for _ in range(5):
            artist.forward(size)
            artist.right(144)
            artist.forward(size)
            artist.left(72)

    artist.end_fill()

# Draw shapes until background is covered
while len(shapes) < 30:  # Adjust the number of shapes as needed
    draw_shape()

# Hide turtle and display
artist.hideturtle()
screen.mainloop()
