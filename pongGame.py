
import turtle

wn = turtle.Screen()  # Create a screen called win
wn.title("Pong")  # Set the title of the screen to be pong
wn.bgcolor("black")  # Set the background of the screen to be black
wn.setup(width=800, height=600)  # Set the width and height of the screen
wn.tracer(0)  # Stops the window from updating, lets us speed up the game

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()  # Turtle object using Turtle class
paddle_a.speed(0)  # Set the speed animation
paddle_a.shape("square")  # Set the shape of the paddle
paddle_a.color("white")  # Set the color of the paddle
paddle_a.shapesize(stretch_wid=5, stretch_len=1)  # stretch the width (5x20)
paddle_a.penup()  # Set the color of the paddle
paddle_a.goto(-350, 0)  # coordinates to start at, left side middle, not touching the border

# Paddle B
paddle_b = turtle.Turtle()  # Turtle object using Turtle class
paddle_b.speed(0)  # Set the speed animation
paddle_b.shape("square")  # Set the shape of the paddle
paddle_b.color("white")  # Set the color of the paddle
paddle_b.shapesize(stretch_wid=5, stretch_len=1)  # stretch the width (5x20)
paddle_b.penup()  # move up
paddle_b.goto(350, 0)  # coordinates to start at

# Ball
ball = turtle.Turtle()  # Turtle object using Turtle class
ball.speed(0)  # Set the speed animation
ball.shape("square")  # Set the shape of the paddle
ball.color("white")  # Set the color of the paddle
ball.penup()  # move up
ball.goto(0, 0)  # coordinates to start at, middle of the screen
ball.dx = 0.2  # Everytime the ball moves, it moves by 0.2 px (right 0.2 px)
ball.dy = 0.2  # Everytime the ball moves, it moves by 0.2 px (up 0.2 px)

# Pen (writing)
pen = turtle.Turtle()  # create pen object
pen.speed(0)  # Set the speed animation
pen.shape("square")  # Shape to square
pen.color("white")  # Color of text
pen.penup()  # Move up
pen.hideturtle()  # Hide it
pen.goto(0, 260)  # Height is 600 so around 260+ top is fine
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))  # Write text


# Functions
def paddle_a_up():  # Function to move paddle up
    y = paddle_a.ycor()  # get the y coordinate of the left paddle
    y += 20  # Add 20 pixels to the y coordinate
    paddle_a.sety(y)  # Set the y coordinate of paddle_left to y (+= 20)


def paddle_a_down():  # Function to move paddle down
    y = paddle_a.ycor()  # get the y coordinate of the left paddle
    y -= 20  # Subtract 20 pixels to the y coordinate
    paddle_a.sety(y)  # Set the y coordinate of paddle_left to y (-= 20)


def paddle_b_up():  # Function to move paddle up
    y = paddle_b.ycor()  # get the y coordinate of the right paddle
    y += 20  # Add 20 pixels to the y coordinate
    paddle_b.sety(y)  # Set the y coordinate of paddle_right to y (+= 20)


def paddle_b_down():  # Function to move paddle down
    y = paddle_b.ycor()  # get the y coordinate of the right paddle
    y -= 20  # Subtract 20 pixels to the y coordinate
    paddle_b.sety(y)  # Set the y coordinate of paddle_right to y (-= 20)


# Keyboard bindings
wn.listen()  # Tells window to listen for keyboard inputs
wn.onkeypress(paddle_a_up, "w")  # on key press W, call paddle_left_up function to move paddle_left up
wn.onkeypress(paddle_a_down, "s")  # on ke press S, call paddle_left_down function to move paddle_left down
wn.onkeypress(paddle_b_up, "Up")  # on key press Up (Arrow) , call paddle_right_up function to move paddle_right up
wn.onkeypress(paddle_b_down,
              "Down")  # on ke press Down (Arrow, call paddle_right_down function to move paddle_right down

# Main game loop
while True:
    wn.update()  # updates the screen everytime the loop runs

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)  # Set the x coordinate to the current x coordinate of the ball, plus the delta x
    ball.sety(ball.ycor() + ball.dy)  # Set the y coordinate to the current y coordinate of the ball, plus the delta y

    # Border checking (compare the ball's x,y coordinate and get it to bounce)

    # Y Axis Top / Bottom (The height of the window is 600px (+300 top, -300 bottom)
    # If past  +- 290, its past the paddle then etc....
    if ball.ycor() > 290:  # Top is +300
        ball.sety(290)  # Set it back to 290
        ball.dy *= -1  # Reverses the direction of the ball

    elif ball.ycor() < -290:  # Bottom is -300
        ball.sety(-290)  # Set it back to -290
        ball.dy *= -1  # Reverses the direction of the ball

    # If past  +- 390, its past the paddle then etc....
    # X Axis  Left / Right (The width of the window is 800px (+400 left, -400 right)
    # Left and right
    if ball.xcor() > 350:  # Left is +350
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)  # put ball back to center
        ball.dx *= -1  # Reverse Direction

    elif ball.xcor() < -350:  # Right is -350
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1  # Reverse Direction

    # Paddle and ball collisions
    if ball.xcor() < -340 and paddle_a.ycor() + 50 > ball.ycor() > paddle_a.ycor() - 50:  # paddle was set to 350, if ball reaches middle of paddle and ball is between the top and bottom of paddle
        ball.dx *= -1

    elif ball.xcor() > 340 and paddle_b.ycor() + 50 > ball.ycor() > paddle_b.ycor() - 50:
        ball.dx *= -1
