import pygame
import consts
import sys
from game_manager import GameManager
from snake import Snake

#defult language
language = 'english'

def main_menu(screen):
    global language
    font = pygame.font.Font(None, 36)
    text_color = (255, 255, 255)
    
    if language == 'english':
        title_text = font.render("Snake Game", True, text_color)
        language_text = font.render("Press 'T' for Turkish", True, text_color)
    else:  # language == 'turkish'
        title_text = font.render("Yılan Oyunu", True, text_color)
        language_text = font.render("İngilizce için 'E' tuşuna basın", True, text_color)
    
    title_rect = title_text.get_rect(center=(consts.width // 2, consts.height // 2 - 50))
    language_rect = language_text.get_rect(center=(consts.width // 2, consts.height // 2 + 50))
    
    screen.blit(title_text, title_rect)
    screen.blit(language_text, language_rect)
    
    pygame.display.flip()

def main():
    pygame.init()
    screen = pygame.display.set_mode((consts.width, consts.height))
    screen.fill(consts.back_color)
    clock = pygame.time.Clock()
    global language
    
    main_menu(screen)
    
    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_t:
                    language = 'turkish'
                    main_menu(screen)
                elif event.key == pygame.K_e:
                    language = 'english'
                    main_menu(screen)
        
        pygame.display.update()
        clock.tick(consts.FPS)

if __name__ == '__main__':
    main()
