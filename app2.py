# import modules
from colorsFonts import *
from Menues import *
from levels import *

# import pygame library and initialise the pygame font
import pygame
pygame.init()
pygame.font.init()

 
# Title and Icon 
pygame.display.set_caption("Awesom Sudoku Game")
img = pygame.image.load('Sudoku/static/icon.jpeg')
pygame.display.set_icon(img)

main_menu = Menu()
main_menu.main_menu()
grid = main_menu.grid
color = main_menu.color

#grid = easy_modifiable_grid

x = 0
y = 0
dif = 500 / 9
val = 0
# Default Sudoku Board.


def get_cord(pos):
    global x
    x = pos[0]//dif
    global y
    y = pos[1]//dif


# Load test fonts for future use


 
# Highlight the cell selected
def draw_box():
    for i in range(2):
        pygame.draw.line(screen, black, (x * dif-3, (y + i)*dif), (x * dif + dif + 3, (y + i)*dif), 7)
        pygame.draw.line(screen, black, ( (x + i)* dif, y * dif ), ((x + i) * dif, y * dif + dif), 7)   
 
# Function to draw required lines for making Sudoku grid         
def draw():
    # Draw the lines
        
    for i in range (9):
        for j in range (9):
            if grid[i][j]!= 0:
 
                # Fill blue color in already numbered grid
                pygame.draw.rect(screen, color, (i * dif, j * dif, dif + 1, dif + 1))
 
                # Fill grid with default numbers specified
                text1 = font1.render(str(grid[i][j]), 1, (0, 0, 0))
                screen.blit(text1, (i * dif + 15, j * dif))
    # Draw lines horizontally and verticallyto form grid           
    for i in range(10):
        if i % 3 == 0 :
            thick = 7
        else:
            thick = 1
        pygame.draw.line(screen, (0, 0, 0), (0, i * dif), (500, i * dif), thick)
        pygame.draw.line(screen, (0, 0, 0), (i * dif, 0), (i * dif, 500), thick)   
 
# Fill value entered in cell      
def draw_val(val, color):
    text1 = font1.render(str(val), 1, color)
    screen.blit(text1, (x * dif + 15, y * dif))    
 
# Raise error when wrong value entered
def raise_error1():
    text1 = font2.render("WRONG !!!", 1, black)
    screen.blit(text1, (5, 550))
    pygame.display.update()
    pygame.time.delay(1000)
 
# Check if the value entered in board is valid
def valid(m, i, j, val):
    for it in range(9):
        if m[i][it]== val:
            return False
        if m[it][j]== val:
            return False
    it = i//3
    jt = j//3
    for i in range(it * 3, it * 3 + 3):
        for j in range (jt * 3, jt * 3 + 3):
            if m[i][j]== val:
                return False
    return True
 
# Solves the sudoku board using Backtracking Algorithm
def solve(grid, i, j):
     
    while grid[i][j]!= 0:
        if i<8:
            i+= 1
        elif i == 8 and j<8:
            i = 0
            j+= 1
        elif i == 8 and j == 8:
            return True
    pygame.event.pump()    
    for it in range(1, 10):
        if valid(grid, i, j, it)== True:
            grid[i][j]= it
            global x, y
            x = i
            y = j
            # white color background\
            screen.fill(white)
            draw()
            draw_box()
            pygame.display.update()
            pygame.time.delay(20)
            if solve(grid, i, j)== 1:
                return True
            else:
                grid[i][j]= 0
            # white color background\
            screen.fill(white)
         
            draw()
            draw_box()
            pygame.display.update()
            pygame.time.delay(50)    
    return False 
 
# Display instruction for the game
def instruction():
    text1 = font2.render("Press C to change the grid color, Q to quit", 1, black)
    text2 = font2.render("Press Enter to go back to levels menu", 1, black)
    text3 = font2.render("Press backspace to delete", 1, black)
    screen.blit(text1, (5, 505))        
    screen.blit(text2, (5, 525))
    screen.blit(text3, (5, 545))
# Display options when solved
def result():
    text1 = font2.render("You solved it, press enter to return to menu", 1, black)
    screen.blit(text1, (20, 570))

# declared values
run = True
flag1 = 0
flag2 = 0
rs = 0
error = 0
clock = pygame.time.Clock()

# The loop thats keep the window running

while run == True:

    # White color background
    screen.fill(white)
    # Loop through the events stored in event.get()
    for event in pygame.event.get():
        # Quit the game window
        if event.type == pygame.QUIT:
            run = False 
        # Get the mouse position to insert number    
        if event.type == pygame.MOUSEBUTTONDOWN:
            flag1 = 1
            pos = pygame.mouse.get_pos()
            get_cord(pos)
        # Get the number to be inserted if key pressed    
        if event.type == pygame.KEYDOWN:
            # use backspace to errase any cell
            if event.key == pygame.K_BACKSPACE:
                if grid[int(x)][int(y)]:
                    grid[int(x)][int(y)] = 0
            if event.key == pygame.K_q:
                run = False
            if event.key == pygame.K_LEFT:
                x-= 1
                flag1 = 1
            if event.key == pygame.K_RIGHT:
                x+= 1
                flag1 = 1
            if event.key == pygame.K_UP:
                y-= 1
                flag1 = 1
            if event.key == pygame.K_DOWN:
                y+= 1
                flag1 = 1   
            if event.key == pygame.K_1:
                val = 1
            if event.key == pygame.K_2:
                val = 2   
            if event.key == pygame.K_3:
                val = 3
            if event.key == pygame.K_4:
                val = 4
            if event.key == pygame.K_5:
                val = 5
            if event.key == pygame.K_6:
                val = 6
            if event.key == pygame.K_7:
                val = 7
            if event.key == pygame.K_8:
                val = 8
            if event.key == pygame.K_9:
                val = 9 
            if event.key == pygame.K_RETURN:     
                main_menu.main_menu()
                grid = [
                    [7, 8, 0, 4, 0, 0, 1, 2, 0],
                    [6, 0, 0, 0, 7, 5, 0, 0, 9],
                    [0, 0, 0, 6, 0, 1, 0, 7, 8],
                    [0, 0, 7, 0, 4, 0, 2, 6, 0],
                    [0, 0, 1, 0, 5, 0, 9, 3, 0],
                    [9, 0, 4, 0, 6, 0, 0, 0, 5],
                    [0, 7, 0, 3, 0, 0, 0, 1, 2],
                    [1, 2, 0, 0, 0, 7, 4, 0, 0],
                    [0, 4, 9, 2, 0, 6, 0, 0, 7]
                ]
                color = main_menu.color
                
            # If C pressed clear the sudoku board
            if event.key == pygame.K_c:
                main_menu.color_page()
                color = main_menu.color

    if flag2 == 1:
        if solve(grid, 0, 0)== False:
            error = 1
        else:
            rs = 1
        flag2 = 0   

    if val != 0:            
        print(x)
        print(y)
        if valid(grid, int(x), int(y), val)==True:
            draw_val(val, black)
            grid[int(x)][int(y)]= val
        else:
            draw()
            draw_val(val, red)
            raise_error1()
        val = 0
        
    if error == 1:
        raise_error1()  
    if rs == 1:
        result()     
    draw()  
    if flag1 == 1:
        draw_box()       
    instruction()    

    # Update window
    pygame.display.update()
    clock.tick()
 
# Quit pygame window    
pygame.quit()     