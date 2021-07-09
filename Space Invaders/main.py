import pygame
import random
import math

# Initialize PyGame
pygame.init()

# Create Game Window            #Width, Height
screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load('background.png')

# Title and Icon
pygame.display.set_caption("Space Invaders")
pygame.display.set_icon(pygame.image.load("ufo.png"))

# Player
playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 480
playerX_change = 0  # change in x coordinates

# Enemy
# Create empty list for enemy properties
enemyImg = []
enemyX = []
enemyY = []
enemyY_change = []
enemyX_change = []
num_of_enemies = 6

# Iterate  6 times creating 6 enemies and append the properties to each enemy
for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0, 735))
    enemyY.append(random.randint(50, 150))
    enemyY_change.append(40)
    enemyX_change.append(4)

# Bullet
bulletImg = pygame.image.load('bullet.png')
bulletX = 0  # Will not move in x direction
bulletY = 480  # At spaceship level, will move in negative direction (towards top)
bulletY_change = 10
bullet_state = "ready"  # Bullet state "Ready" - cannot see bullet, "fire" - bullet i moving

# Score
score_value = 0
font = pygame.font.SysFont('Poppins', 32)
textX = 10
textY = 10

# Game Over Text
over_font = pygame.font.SysFont('Poppins', 64)


# Function to show text on screen
def show_score(x, y):
    score = font.render("Score: " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


# Function to show Game Over
def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (250, 250)) #Show in middle of screen


# Player Function To Draw on Screen
def player(x, y):
    screen.blit(playerImg, (x, y))  # Drawing an image of player on screen


# Enemy Function To Draw on Screen
def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


# Function to draw bullet if not fired
def fire_bullet(x, y):
    global bullet_state  # Need it to be global to access in function
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))  # To make sure the bullet appears at the center of the spaceship


# Bullet and Enemy Collision
def isCollision(enemyX, enemyY, bulletX, bulletY):  # Check distance between enemy and bullet
    distance = math.sqrt(
        (math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2)))  # distance between two points
    if distance < 27:  # check if collision occurs
        return True
    return False


# Game Loop
running = True
while running:

    # Screen Fill (RGB)
    screen.fill((0, 0, 0))
    # Background Image
    screen.blit(background, (0, 0))  # Draw the variable image, and write coordinates

    # Events
    for event in pygame.event.get():  # Get all the events and loop over them
        if event.type == pygame.QUIT:  # If the event is quit (close button being pressed)
            running = False  # Set running to false

        # Keyboard Bindings
        if event.type == pygame.KEYDOWN:  # CHECK IF KEY STROKE IS PRESSED (KEYDOWN)
            if event.key == pygame.K_LEFT:  # Check if its a left arrow
                playerX_change = -5  # What the X coordinates will change by (left 0.3)
            if event.key == pygame.K_RIGHT:  # Check if its a right arrow
                playerX_change = +5  # move in x direction 0.3 right
            if event.key == pygame.K_SPACE:  # Check if space key is pressed
                # Only allow to fire if ready (not fire state), checks if bullet is on screen or not
                if bullet_state == "ready":
                    bulletX = playerX  # Get current x coordinate of spaceship and save it to bulletX
                    fire_bullet(bulletX, bulletY)  # call fire_bullet function (changes state to fire)

        if event.type == pygame.KEYUP:  # CHECK IF KEY IS RELEASED
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:  # Check if its a left or right arrow
                playerX_change = 0  # change will be 0, stop moving

    # Call Player Function
    playerX += playerX_change  # Add the change difference of the X coordinate to the spaceship

    # Border Collision
    if playerX <= 0:  # If it goes past the left side, set the x coordinate to 0
        playerX = 0
    elif playerX >= 736:  # If it goes past the right side, set x coordinate to 736 (take in spaceship size to account)
        playerX = 736

    # Border Collision Enemy
    # Use a loop so the program knows what enemy we are talking about

    for i in range(num_of_enemies):

        # Game Over Condition
        if enemyY[i] > 440:  # when one of the enemies reaches the spaceship
            for j in range(num_of_enemies):  # take all the enemies
                enemyY[j] = 2000  # hide the enemies from the screen
            game_over_text()
            break

        enemyX[i] += enemyX_change[i]

        if enemyX[i] <= 0:
            enemyX_change[i] = 4  # Move right when hitting left border
            enemyY[i] += enemyY_change[i]  # Drop 40 px when hitting the border
        elif enemyX[i] >= 736:
            enemyX_change[i] = -4  # Move left when hitting right border
            enemyY[i] += enemyY_change[i]

        # Collision Check (use [i] to make sure program knows what enemy we are talking about)
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)  # pass in current points of loop
        if collision:  # if is collision returns True (collision has occurred)
            # Reset to default points of bullet
            bulletY = 480
            bullet_state = "ready"
            score_value += 1  # Increment score everytime we hit enemy
            # Reset enemy to new positions
            enemyX[i] = random.randint(0, 735)
            enemyY[i] = random.randint(50, 150)

        # Draw the enemy
        enemy(enemyX[i], enemyY[i], i)  # i to specify which enemy is being printed

    # Bullet Movement
    # Create multiple bullets
    if bulletY <= 0:  # If the bullet is past 0 (over the top)
        bulletY = 480  # Reset to its original position
        bullet_state = "ready"

    if bullet_state == "fire":
        fire_bullet(bulletX,
                    bulletY)  # Current position of bulletX which is set to playerX when bullet is fired, bullet y(head of spaceship)
        # Prevents bullet from moving when fired
        bulletY -= bulletY_change  # Move bullet up

    # Pass in the final coordinates to the drawing on screen functions
    player(playerX, playerY)

    # Show score
    show_score(textX, textY)

    # Keep updating
    pygame.display.update()
