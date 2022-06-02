import pygame, sys
from button import Button

pygame.init()
pygame.mixer.pre_init()
pygame.mixer.init()
import os

# start playing the background music
pygame.mixer.music.load(os.path.join(os.getcwd(), 'BackGroundMusic_Menu.mp3'))
pygame.mixer.music.set_volume(0.8)
pygame.mixer.music.play(-1)

win = pygame.display.set_mode((700, 500))
pygame.display.set_caption("B'Pong")

BG = pygame.image.load("background-awal.png")

def func_petunjuk():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
        img_petunjuk = pygame.image.load("foto-petunjuk.png")
        win.blit(img_petunjuk, (0, 0))
        pygame.display.update()

def main_menu():
    while True:
        win.blit(BG, (0, 0))

        mouse_pos = pygame.mouse.get_pos()

        arena1 = Button(image=pygame.image.load("arena 1.png"), pos=(700//2, 270))
        arena2 = Button(image=pygame.image.load("arena 2.png"), pos=(700//2, 330))
        petunjuk = Button(image=pygame.image.load("petunjuk.png"), pos=(700//2, 390))

        for button in [arena1, arena2, petunjuk]:
            button.update(win)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if arena1.checkForInput(mouse_pos):
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound("sfx_button_clik.wav"), maxtime=2000)
                    pygame.mixer.music.pause()
                    import game-1
                    game-1.run = True
                if arena2.checkForInput(mouse_pos):
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound("sfx_button_clik.wav"), maxtime=2000)
                    pygame.mixer.music.pause()
                    import game-2
                    game-2.run = True
                if petunjuk.checkForInput(mouse_pos):
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound("sfx_button_clik.wav"), maxtime=2000)
                    func_petunjuk()

        pygame.display.update()

main_menu()
