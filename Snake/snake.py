import turtle
import time
import random

# variables
delay = 0.1
score = 0
high_score = 0

# Screen setup
wn = turtle.Screen()  # Initialize screen
wn.title('Snake Game')  # Set title of screen
wn.bgcolor("black")  # Set the background color of screen
wn.setup(width=600, height=600)  # Set the size of the screen
wn.tracer(0)  # Turn off the animations

# Snake Head
head = turtle.Turtle()
head.shape('square')  # Set the shape
head.speed(0)  # Not the actual speed, but the speed of the module
head.color('white')
head.penup()  # Does not draw any lines
head.goto(0, 0)  # Start at the center of screen
head.direction = "stop"  # Sit in the middle

# Snake Food
food = turtle.Turtle()
food.shape('circle')  # Set the shape
food.speed(0)  # Not the actual speed, but the speed of the module
food.color('red')
food.penup()  # Does not draw any lines
food.goto(0, 100)  # Start at 0, 100

# Snake Body
segments = []  # Body has segments, will be set to 0 initially

# Score
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()  # not drawing any lines
pen.hideturtle()
pen.goto(0, 260)
pen.write('Score: 0  High Score: 0', align="center", font=("Poppins", 24, "normal"))


# Functions
def go_up():  # change direction of head
    if head.direction != "down":  # prevent reverse order to stop collision (will not let me go down if im up)
        head.direction = "up"


def go_down():
    if head.direction != "up":  # prevent reverse order to stop collision (will not let me go down if im up)
        head.direction = "down"


def go_left():
    if head.direction != "right":  # prevent reverse order to stop collision (will not let me go down if im up)
        head.direction = "left"


def go_right():
    if head.direction != "left":  # prevent reverse order to stop collision (will not let me go down if im up)
        head.direction = "right"


# Moving the snake
def move():
    if head.direction == "up":  # if the direction is up
        y = head.ycor()  # get the current y coordinate of the head
        head.sety(y + 20)  # Increment the current y coordinate by 20

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)


# Keyboard Bindings
wn.listen()  # Listen for key presses, connected to functions
wn.onkeypress(go_up, "w")  # Set the head.direction to up using the go_up function when w is pressed
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

# Main game loop
while True:
    wn.update()  # Keep updating screen

    # Check for border collision (600 x 600) (+300 and -300)
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)  # Pause game 1 second
        head.goto(0, 0)  # Send the head back to the middle
        head.direction = "stop"  # stop the snake

        # Hide the segments
        for segment in segments:  # Goes through list of segments
            segment.goto(1000, 1000)  # Hiding the old segments far away from the screen

        # Clear the segments list
        segments.clear()

        #Reset score
        score = 0
        pen.clear()
        pen.write("Score: {}   High Score: {}".format(score, high_score), align="center", font=("Poppins", 24, "normal"))

        #Reset delay
        delay = 0.1

    # Ball and snake collision
    if head.distance(food) < 20:  # each turtle is 20 pixels w x h, if distance between head and food < 20 (collision)
        # Move the food to a random location
        x = random.randint(-290, 290)  # Screen was 600 x 600 (+300, -300)
        y = random.randint(-290, 290)
        food.goto(x, y)  # Place the food in the random location x and y

        # Increase the body segments
        new_segment = turtle.Turtle()  # Create a new segment (body part)
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("white")
        new_segment.penup()  # Make sure it doesnt draw on the screen
        segments.append(new_segment)  # Append the new body part (new_segment) to body (segment)

        #Shorten the delay to speed game up
        delay -= 0.001

        # Increase the score
        score += 10
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("Score: {}   High Score: {}".format(score, high_score), align="center", font=("Poppins", 24, "normal"))

    # Connection Body (Move the end segments first)
    # Move the tail to the front (last segment goes to the 2nd last segment)
    for index in range(len(segments) - 1, 0, -1):  # Start at length - 1, goes to 0 (+1) and then go down by 1 each time
        x = segments[
            index - 1].xcor()  # I want segment 9 to move where segment 8 was so (index = 9, 9 - 1 = 8) and get the x cor and set it to x
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)  # set the segments coordinates with x and y

    # To move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()  # The move function is called which looks at the head direction which is connected to the go_up etc.. functions

    # Check for collisions between head and segments (lose)
    for segment in segments:
        if segment.distance(head) < 20:  # if distance between segment and head < 20 (collision)
            time.sleep(1)
            head.goto(0, 0)  # send back to middle
            head.direction = "stop"  # stop snake

            for segment in segments:  # Goes through list of segments
                segment.goto(1000, 1000)  # Hiding the old segments far away from the screen

            # Clear the segments list
            segments.clear()

            # Reset score
            score = 0
            pen.clear()
            pen.write("Score: {}   High Score: {}".format(score, high_score), align="center",
                      font=("Poppins", 24, "normal"))

            # Reset delay
            delay = 0.1

    time.sleep(delay)  # Sleep delay
