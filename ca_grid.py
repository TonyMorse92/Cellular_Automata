# First pass. Just doing 1D rule 1 to start off (should just alternate each generation)
# Just going to start off with 10x10 board with cell a_15 initialized black

import pygame
import sys
import time #DEBUGGING


BLACK = (0,0,0)
WHITE = (255,255,255)
GREY = (128,128,128)
ROWS = 400
COLUMNS = 400
CELL_SIZE = 40
STATE = [0,0,0,0,0,1,0,0,0,0] # 1 black
GEN_NUM = 0


def get_input():
    SCREEN_WIDTH = int(input("Input the size of your screen(multiple of 10): "))
    SCREEN_HEIGHT = SCREEN_WIDTH
    CELL_SIZE = SCREEN_WIDTH/10
    return SCREEN_WIDTH,SCREEN_HEIGHT,CELL_SIZE

def main():
    global SCREEN, CLOCK, GEN_NUM, STATE
    pygame.init()
    SCREEN = pygame.display.set_mode((ROWS,COLUMNS))
    CLOCK = pygame.time.Clock()
    SCREEN.fill(WHITE)

    i = 0
    #GEN_NUM = 0
    #STATE = [0,0,0,0,0,1,0,0,0,0]
    draw_grid()
    #while True:
    while i < 10:
        #draw_grid()
        draw_state()
        GEN_NUM += 1
        update_state()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        
        time.sleep(1)
        i += 1

def draw_grid():
    for col in range(COLUMNS):
    #for col in range(5):
        for row in range(ROWS):
       #for row in range(1):
            grid = pygame.Rect(row*CELL_SIZE, col*CELL_SIZE,CELL_SIZE,CELL_SIZE)
            

            pygame.draw.rect(SCREEN, GREY, grid, 1)


def draw_state():
    global GEN_NUM
    #print(f"STATE[5] should be 1. It is {STATE[5]}")
    #print(f"The STATE is: {STATE}")
    #print(f"Length of state: {len(STATE)}")
    for i in range(len(STATE)):
        #print(f"is 1?:{STATE[i]} --> {STATE[i] == 1}")
        if STATE[i] == 1:
            #print(f"i: {i}")
            # This will be drawing the colors for the current generation
            generation = pygame.Rect(i*CELL_SIZE,GEN_NUM*CELL_SIZE,CELL_SIZE,CELL_SIZE)

            pygame.draw.rect(SCREEN, BLACK, generation, 0)

def update_state():
    global STATE
    # This will be updating creating the new generation based on the rule of the last generation
    # As noted at top, initially this will just be for rule 1, but will eventually modify to make rules selectable
    NEW_STATE = [0]*len(STATE)

    # Always flip the endpoints
    NEW_STATE[0] = (STATE[0]+1) % 2
    NEW_STATE[len(STATE)-1] = (STATE[len(STATE)-1]+1) % 2

    for i in range(1,len(STATE)-1):
        # Only way for a bit to flip in RULE 1 is if they are all 0
        if(STATE[i-1] + STATE[i] + STATE[i+1] == 0):
            NEW_STATE[i] = 1

    #print(f"State: {STATE}")
    #print(f"Newst: {NEW_STATE}")
    STATE = NEW_STATE

main()
