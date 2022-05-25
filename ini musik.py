# Imports and inits
import pygame
pygame.init()
from pygame import mixer
mixer.init()

# Window setup
win = pygame.display.set_mode((750, 500))
pygame.display.set_caption("B'Pong")
background_image1 = pygame.image.load('fancy-court.png')
background_image2 = pygame.image.load('court 2.jpeg')

#Background Sound
mixer.music.load('The-Beginning-w-Caturday.mp3')
mixer.music.play()

# Colors
white = (255, 255, 255)
black = (0, 0, 0)

# Sprite Classes

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('paddle glow.png')
        self.rect = self.image.get_rect()
        self.points = 0

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('ball glow.png')
        self.rect = self.image.get_rect()
        self.speed = 22
        self.dx = 1
        self.dy = 1

class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([20, 30])
        self.image.fill(white)
        self.rect = self.image.get_rect()
        self.rect.center = (750/2, 500)
        self.speed = 5
    
    def bergerak(self):
        while self.rect.y > 0 :
            self.rect.y -= self.speed

    def update():
        pass

"""class Skill(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 
    
    def slower():
        pass

    def faster():
        pass

    def bonus_poin():
        pass
"""

# Sprite Creation

player1 = Player()
player2 = Player()

player_speed = 30

player1.rect.x = -5
player1.rect.y = 225

player2.rect.x = 700
player2.rect.y = 225

pong = Ball()
pong.rect.x = 375
pong.rect.y = 250

obstacle = Obstacle()

# Group of Sprites
all_sprites = pygame.sprite.Group()
all_sprites.add(player1, player2, pong)

# Fungsi tampilan screen
def redraw():
    # Draw background
    win.fill(black)
    win.blit(background_image1, (0, 0))
    pygame.display.update()

    # Font judul
    font = pygame.font.SysFont('Comic Sans MS', 30)
    text = font.render('PONG GAME', False, white)
    textRect = text.get_rect()
    textRect.center = (750 // 2, 25)
    win.blit(text, textRect)

    # Score Player 1 
    p1_score = font.render(str(player1.points), False, white)
    p1Rect = p1_score.get_rect()
    p1Rect.center = (50, 50)
    win.blit(p1_score, p1Rect)

    # Score Player 2 
    p2_score = font.render(str(player2.points), False, white)
    p2Rect = p2_score.get_rect()
    p2Rect.center = (700, 50)
    win.blit(p2_score, p2Rect)

    # Update Sprites
    all_sprites.draw(win)

    # Draw updates
    pygame.display.update()

run = True

# Main Loop
while run:

    pygame.time.delay(100)

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
    
    if pong.rect.y > 490:
        pong.dy = -1

    if pong.rect.y < 1:
        pong.dy = 1

    if pong.rect.x > 740:
        pong.rect.x, pong.rect.y = 375, 250
        pong.dx = -1
        player1.points += 1
        sound = mixer.Sound('Score.mp3')
        sound.play()

    if pong.rect.x < 1:
        pong.rect.x, pong.rect.y = 375, 250
        pong.dx = 1
        player2.points += 1

    if player1.rect.colliderect(pong.rect):
        pong.dx = 1

    if player2.rect.colliderect(pong.rect):
        pong.dx = -1

    if player1.points == 10:
        player2.kill()

    if player2.points == 10:
        player1.kill()
    # Runs redraw function above
    redraw()

pygame.quit()