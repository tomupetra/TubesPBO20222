import pygame, sys
from button import Button

pygame.init()

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
                    import pong_game
                    pong_game.run = True
                if arena2.checkForInput(mouse_pos):
                    import pong_pong
                    pong_pong.run = True
                if petunjuk.checkForInput(mouse_pos):
                    func_petunjuk()

        pygame.display.update()

main_menu()
