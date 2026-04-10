import turtle

screen = turtle.Screen()
screen.bgcolor("lightblue")  # Setting background color
screen.title("Python Polygon Drawing")

t = turtle.Turtle()
t.shape("turtle")
t.speed(3)
t.width(2)

def draw_polygon(sides, length, color, x, y):
    t.penup()
    t.goto(x, y)      
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    
    angle = 360 / sides
    
    for _ in range(sides):
        t.forward(length)
        t.left(angle)
        
    t.end_fill()

draw_polygon(3, 100, "yellow", -150, 0)

draw_polygon(4, 100, "orange", 0, 0)

draw_polygon(6, 70, "lightgreen", 150, 0)

t.hideturtle()
screen.exitonclick()