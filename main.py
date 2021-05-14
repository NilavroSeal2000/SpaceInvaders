import pygame
import random
import math

# Initialise the game library
pygame.init()

# Create the screen of width 800 pixel and height 600 px
screen = pygame.display.set_mode((910, 512))

# Title and Icon  Store png image in this folder
pygame.display.set_caption("Space_Invaders")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# Background information
bg = pygame.image.load('background.png').convert()

# Player info
playerImg = pygame.image.load('player1.png')  # Check the size of the image
playerX = 450
playerY = 410
playerChangeX = 0

# Enemy info
# enemyImg = pygame.image.load('enemy1.png')  # Check the size of the image
# enemyX = random.randint(0, 735) # because of 108 no line
# enemyY = random.randint(0, 150)
# enemyChangeX = 0.3
# enemyChangeY = 30
enemyImg = []
enemyX = []
enemyY = []
enemyChangeX = []
enemyChangeY = []
num_of_enemy = 12
for i in range(num_of_enemy):
    enemyImg.append(pygame.image.load('enemy1.png'))  # Check the size of the image
    enemyX.append(random.randint(0, 735))  # because of 108 no line
    enemyY.append(random.randint(0, 150))
    enemyChangeX.append(0.3)
    enemyChangeY.append(30)

# Bullet info
# Two states of bullet ---
# Ready : You cant see the bullet
# Fire : The bullet is currently moving

bulletImg = pygame.image.load('bullet1.png')  # Check the size of the image
bulletX = 0
bulletY = 350
bulletChangeX = 0
bulletChangeY = 3
bullet_state = "ready"


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


def fire(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 35, y + 100))  # From where bullet will fire


def inCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX - 15 - bulletX, 2)) + (math.pow((enemyY - 100) - bulletY, 2)))
    if distance < 30:
        return True
    else:
        return False


# Players score
score = 0  # For Terminal

score_value = 0  # For The window
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10


def show_score(x, y):
    score = font.render("Score:" + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


# Game Over Text
over = pygame.font.Font('freesansbold.ttf', 64)


def game_over_text():
    game_over = over.render("GAME OVER", True, (255, 255, 255))
    screen.blit(game_over, (280, 200))


# Game Loop if close button pressed the game will be closed
running = True

while running:
    # Background screen colour in RGB( 0 to  255)
    screen.fill((0, 100, 100))
    # background image
    screen.blit(bg, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # If any keystroke pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                playerChangeX = 1
            if event.key == pygame.K_LEFT:
                playerChangeX = -1
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletX = playerX
                    fire(bulletX, bulletY)  # other wise if we use playerX bullet will move with player position
        # if key is released
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerChangeX = 0
    playerX += playerChangeX

    # Boundary of Spacecraft
    if playerX <= 0:
        playerX = 0
    if playerX >= 700:
        playerX = 700

    # Enemy Movement Boundrary for the enemy
    for i in range(num_of_enemy):
        # Game Over
        if (enemyY[i] > 300):
            for j in range(num_of_enemy):
                enemyY[j] = 2000  # All enemy will go out of screen
            game_over_text()
            break
        enemyX[i] += enemyChangeX[i]
        if enemyX[i] <= 0:
            enemyChangeX[i] = 0.3
            enemyY[i] += enemyChangeY[i]
        if enemyX[i] >= 736:
            enemyChangeX[i] = -0.3
            enemyY[i] += enemyChangeY[i]
        # Collision occures or not
        collision = inCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            bulletY = 350
            bullet_state = "ready"
            score += 1
            score_value += 10
            print(score)
            enemyX[i] = random.randint(0,
                                       735)  # Otherwise enemey will fall down when it will reach more than 736 for 108 line
            enemyY[i] = random.randint(0, 150)
        enemy(enemyX[i], enemyY[i], i)

    # Bullet Movement
    if bulletY <= -100:
        bulletY = 350
        bullet_state = "ready"

    if bullet_state is "fire":
        fire(bulletX, bulletY)
        bulletY -= bulletChangeY

    player(playerX, playerY)
    show_score(textX, textY)  # It will show the message in textX,textY position
    pygame.display.update()  # Otherwise colour will not change
