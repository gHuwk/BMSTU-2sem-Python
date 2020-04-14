import pygame
import math
import sys

def main():

    def box(begin_xy):
        begin_x, begin_y = begin_xy
        pygame.draw.rect(screen, constants("NORM_GRAY"), (begin_x, begin_y, 100, 100))
        pygame.draw.lines(screen, constants("BLACK"), True, [[begin_x, begin_y], [begin_x + 100, begin_y], \
                                                       [begin_x + 100, begin_y + 100], [begin_x, begin_y + 100]], 2)
    
    # Const
    FPS = constants("FPS")
    
    pygame.init()                                             # инициализируем pygame
    pygame.display.set_caption("Animation")                   # Шапка
    screen = resolutionPyGame()                               # установка дисплея
    
    clock = pygame.time.Clock()                               # объект времени. Можно через delay.
    essentialFigures(screen)
    pygame.display.update()                                   # обновляем дисплей

    begin_box_x = 40
    begin_box_y = 575

    while True:
        events = pygame.event.get()                           # events содержит список событий
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()                                    # выход при нажатии на кнопку или alt-F4

        box((begin_box_x, begin_box_y))
        #animation(screen)
        pygame.display.update()
        
        if (begin_box_x < 1395):
            begin_box_x += 10

        clock.tick(FPS)                                       # частота остановки 60 FPS
        essentialFigures(screen)
        
def constants(initial):
    # Frame per second
    const = {
             "FPS": 60,
             "FULLHD_RESOLUTION": (1920,1080),
             "STANDART_RESOLUTION": (640, 360),
             "WHITE": (255, 255, 255),
             "BLACK": (0, 0, 0),
             "GRAY": (125, 125, 125),
             "GRAY_ART_LEBEDEV": (51, 51, 51),
             "LIGHT_BLUE": (64, 128, 255),
             "GREEN": (0, 200, 64),
             "YELLOW": (225, 225, 0),
             "PINK": (230, 50, 230),
             "ROYAL_ORANGE": (249, 129, 42),
             "BROWN": (102, 51, 0),
             "BACKGROUND_ART_LEBEDEV_01": (255,255,204),
             "BROWN_ART_LEBEDEV": (205,153,0),
             "RED": (255, 0, 0),
             "BLUE": (0, 0, 255),
             "NORM_GRAY": (180, 180, 180)
             }
    return const[initial]

    
def resolutionPyGame():
    # Инициализация screen объекта для работы и возврат генерируемого оного
    #print("Initializate in fullscreen? (Y/N) ignore=N: ")
    #answer = input()
    answer = "Y"
    if answer == "Y":
        # Запуск с аппаратным ускорением и полным экраном
        screen = pygame.display.set_mode(constants("FULLHD_RESOLUTION"), pygame.HWSURFACE|pygame.FULLSCREEN)
    else:
        # Только аппартаное ускорение
        screen = pygame.display.set_mode(constants("STANDART_RESOLUTION"), pygame.HWSURFACE)
    return screen

def essentialFigures(screen):
    
    # background
    screen.fill(constants("BACKGROUND_ART_LEBEDEV_01"))
    
    def desktop():
        # desktop 1
        pygame.draw.polygon(screen, constants("BROWN_ART_LEBEDEV"),[[40, 675], [1880, 675], [1880, 725], [40, 725]])
        # desktop 2
        pygame.draw.polygon(screen, constants("BROWN_ART_LEBEDEV"),[[200, 860], [1720, 860], [1720, 900], [200, 900]])
        # foot 1
        pygame.draw.polygon(screen, constants("BROWN_ART_LEBEDEV"),[[160, 725], [200, 725], [200, 1080], [160, 1080]])
        # foot 2
        pygame.draw.polygon(screen, constants("BROWN_ART_LEBEDEV"),[[1720, 725], [1760, 725], [1760, 1080], [1720, 1080]])
        # lines
        pygame.draw.lines(screen, constants("GRAY_ART_LEBEDEV"),True,[[40, 675], [1880, 675], [1880, 725], [40, 725]], 4)
        pygame.draw.lines(screen, constants("GRAY_ART_LEBEDEV"),True,[[200, 860], [1720, 860], [1720, 900], [200, 900]], 4)
        pygame.draw.lines(screen, constants("GRAY_ART_LEBEDEV"),True,[[160, 725], [200, 725], [200, 1080], [160, 1080]], 4)
        pygame.draw.lines(screen, constants("GRAY_ART_LEBEDEV"),True,[[1720, 725], [1760, 725], [1760, 1080], [1720, 1080]], 4)

    def magnet():
        # part 1
        pygame.draw.rect(screen, constants("GRAY"), (1500, 475, 180, 200))
        pygame.draw.circle(screen, constants("GRAY"), (1680, 575), 100)
        pygame.draw.rect(screen, constants("RED"), (1500, 475, 65, 100))
        pygame.draw.rect(screen, constants("BLUE"), (1500, 575, 65, 100))
        pygame.draw.rect(screen, constants("BACKGROUND_ART_LEBEDEV_01"), (1500, 525, 180, 100))
        pygame.draw.circle(screen, constants("BACKGROUND_ART_LEBEDEV_01"), (1680, 575), 50)
        
    desktop()
    magnet()

def aalineWithThickness(sc, colour, begin, end, thickness, direction):
    # draw in range of thickness good lines
    # dont mind for what
    # its useless
    i = 0
    while i < thickness:
        if direction == 1:
            # вверх
            begin[0],begin[1] = begin[0], begin[1] + i
            end[0], end[1] = end[0], end[1] + i
        elif direction == 2:
            # вниз
            begin[0],begin[1] = begin[0], begin[1] - 20
            end[0], end[1] = end[0] -20, end[1] - 20
        elif direction == 3:
            # вправо
            begin[0],begin[1] = begin[0] + i, begin[1]
            end[0], end[1] = end[0] + i, end[1]
        elif direction == 4:
            # влево
            begin[0],begin[1] = begin[0] - i, begin[1]
            end[0], end[1] = end[0] - i, end[1]
        #print(begin, end)
        pygame.draw.aaline(sc, colour, begin, end)
        i+=1
        

if __name__ == "__main__":
    main()
