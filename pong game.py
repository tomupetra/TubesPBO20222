# Imports and inits
import pygame
pygame.init()
import sys
from tkinter import *
from tkinter import messagebox
Tk().wm_withdraw()

clock = pygame.time.Clock()
# Window setup
win = pygame.display.set_mode((750, 500))
pygame.display.set_caption("B'Pong")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)

# Sprite Classes

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([10, 75])
        self.image = pygame.image.load('paddle_glow.png')
        self.rect = self.image.get_rect()
        self.points = 0

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('ball_glow.png')
        self.rect = self.image.get_rect()
        self.speed = 15
        self.dx = 1
        self.dy = 1


# Sprite Creation

player1 = Player()
player2 = Player()

player_speed = 15

player1.rect.x = 0
player1.rect.y = 225

player2.rect.x = 710
player2.rect.y = 225

pong = Ball()
pong.rect.x = 375
pong.rect.y = 250

# Group of Sprites
all_sprites = pygame.sprite.Group()
all_sprites.add(player1, player2, pong)


bg_image1 = pygame.image.load('fancy_court.png')
bg_image2 = pygame.image.load('court_2.jpeg')
# Screen update function
def redraw():

    win.fill(black)
    win.blit(bg_image1, (0, 0))
    pygame.display.update()

    # Title font
    font = pygame.font.SysFont('Comic Sans MS', 30)
    text = font.render('PONG', False, white)
    textRect = text.get_rect()
    textRect.center = (750 // 2, 25)
    win.blit(text, textRect)

    # Player 1 Score
    p1_score = font.render(str(player1.points), False, white)
    p1Rect = p1_score.get_rect()
    p1Rect.center = (50, 50)
    win.blit(p1_score, p1Rect)

    # Player 2 Score
    p2_score = font.render(str(player2.points), False, white)
    p2Rect = p2_score.get_rect()
    p2Rect.center = (700, 50)
    win.blit(p2_score, p2Rect)

    # Updates all Sprites
    all_sprites.draw(win)

    # Draws updates
    pygame.display.update()

run = True
# Main Loop
while run :
    clock.tick(60)
    pygame.time.delay(50)

    # Quit Event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Player Movement
    key = pygame.key.get_pressed()
    if key[pygame.K_w]:
        player1.rect.y += -player_speed
    if key[pygame.K_s]:
        player1.rect.y += player_speed
    if key[pygame.K_UP]:
        player2.rect.y += -player_speed
    if key[pygame.K_DOWN]:
        player2.rect.y += player_speed

    # Moves pong ball
    pong.rect.x += pong.speed * pong.dx
    pong.rect.y += pong.speed * pong.dy

    # Wall and Player Bounces
    if pong.rect.y > 450:
        pong.dy = -1

    if pong.rect.y < 1:
        pong.dy = 1

    if pong.rect.x > 740:
        pong.rect.x, pong.rect.y = 375, 250
        pong.dx = -1
        player1.points += 1

    if pong.rect.x < 1:
        pong.rect.x, pong.rect.y = 375, 250
        pong.dx = 1
        player2.points += 1

    if player1.rect.colliderect(pong.rect):
        pong.dx = 1

    if player2.rect.colliderect(pong.rect):
        pong.dx = -1

    # Shortcut to End the Game
    if key[pygame.K_o]:     # 'o' stands for over
        run = False
    
    # Shortcut to End the Game
    if player1.points ==  10:
        run = False
        messagebox.showinfo('Game Over',"Congratulations!\nPlayer 1 Win!")
    if player2.points == 10:
        run = False
        messagebox.showinfo('Game Over',"Congratulations!\nPlayer 2 Win!")
    
    # shortcut to make player 1 win
    if key[pygame.K_1]:
        player1.points = 10

    # shortcut to make player 2 win
    if key[pygame.K_2]:
        player2.points = 10

    # Runs redraw function above
    redraw()

pygame.quit()
