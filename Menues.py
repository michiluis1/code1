#import modules
from colorsFonts import *
from levels import *

import pygame
pygame.init()

screen = pygame.display.set_mode((500, 600))

# Menues Class
class Menu:
    # constructor with grid and color atributes
    def __init__(self, grid = [], color = (0, 0, 0)):
        self.grid = grid
        self.color = color
    
    # Function that creates a main menu
    def main_menu(self):
        screen.fill(white)
        title_text = title_font.render("Sudoku", 1, black)
        screen.blit(title_text, (500 // 2 - title_text.get_width() // 2, 100))
        start = font.render('Start', 1, black)  # White text
        start_button = pygame.Rect(200,200,110,60)
        options = font.render('Levels', 1, black) 
        options_button = pygame.Rect(200,300,110,60)
        colors = font.render('Colors', 1, black) 
        colors_button = pygame.Rect(200,400,110,60)


        a,b = pygame.mouse.get_pos()
        
        if start_button.x <= a <= start_button.x + 110 and start_button.y <= b <= start_button.y + 60:
            pygame.draw.rect(screen,(230,230,230),start_button)
        else:
            pygame.draw.rect(screen,(180,180,180),start_button)
        screen.blit(start,(start_button.x +5, start_button.y +5))
            #waiting_for_start = False
        if options_button.x <= a <= options_button.x + 110 and options_button.y <= b <= options_button.y + 60:
            pygame.draw.rect(screen,(230,230,230),options_button)
                        
        else:
            pygame.draw.rect(screen,(180,180,180),options_button)        
        screen.blit(options,(options_button.x +5, options_button.y +5))
        if colors_button.x <= a <= colors_button.x + 110 and colors_button.y <= b <= colors_button.y + 60:
            pygame.draw.rect(screen,(230,230,230),colors_button)
        else:
            pygame.draw.rect(screen,(180,180,180),colors_button)
        screen.blit(colors,(colors_button.x +5, colors_button.y +5))

        pygame.display.update()

        # Declaring a True value for while loop
        waiting_for_start = True
        while waiting_for_start == True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    
                    if start_button.collidepoint(event.pos):
                        self.grid = easy_modifiable_grid
                        self.color = darkGray
                        waiting_for_start = False
                        return self.grid, self.color

                    elif options_button.collidepoint(event.pos):
                        self.levels_page() # call levels_page() function
                        waiting_for_start = False
                    elif colors_button.collidepoint(event.pos):
                        self.color_page() # calls color_page() function
                        waiting_for_start = False
    
    # Levels manu page                   
    def levels_page(self):
        screen.fill((200, 200, 250))

        # Setting up the title of the board
        title_text = title_font.render("Sudoku", 1, black)
        screen.blit(title_text, (500 // 2 - title_text.get_width() // 2, 100))

        # Instruction for the user
        instruction_text = instruction_font.render("Choose difficulty level:", 1, black)
        screen.blit(instruction_text, (500 // 2 - instruction_text.get_width() // 2, 190))

        # Creating the buttons form this menue
        easy_scheme = pygame.Rect(100, 270, 80, 50)
        medium_scheme = pygame.Rect(210, 270, 80, 50)
        hard_scheme = pygame.Rect(305,270,80,50)
        
        # Drawing the buttons to screen
        pygame.draw.rect(screen, black, easy_scheme)
        pygame.draw.rect(screen, black, medium_scheme)
        pygame.draw.rect(screen, black, hard_scheme)
        
        # possition and text of the button
        easy_scheme_text = instruction_font.render("Easy", 1, white)
        screen.blit(easy_scheme_text, (120, 280))

        # possition and text of the button
        medium_scheme_text = instruction_font.render("Medium", 1, white)
        screen.blit(medium_scheme_text, (215, 280))

        # possition and text of the button
        hard_scheme_text = instruction_font.render("Hard", 1, white)
        screen.blit(hard_scheme_text, (325, 280))

        # update the screen
        pygame.display.update()

        waiting_for_start = True
        while waiting_for_start == True:
            for event in pygame.event.get():
                # listening for quit actions
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.type == pygame.K_RETURN:
                        pygame.quit()
                        quit()
                # listening for mouse clicks
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    # calling difficulty of board
                    if easy_scheme.collidepoint(mouse_pos):
                        print("Easy mode selected")
                        self.grid = easy_modifiable_grid
                        self.color_page()
                        waiting_for_start = False
                        return self.grid
                    
                    # calling difficulty of board
                    elif medium_scheme.collidepoint(mouse_pos):
                        print("Medium level")
                        self.grid = medium_modifiable_grid
                        self.color_page()
                        waiting_for_start = False
                        return self.grid
                    
                    # calling difficulty of board
                    elif hard_scheme.collidepoint(mouse_pos):
                        print("Hard level")
                        self.grid = hard_modifiable_grid
                        self.color_page()
                        waiting_for_start = False
                        return self.grid
                    
    # Colors menu page
    def color_page(self):
        # fill in screen with color
        screen.fill((200, 200, 200))

        # Title of the colors menu page
        title_text = title_font.render("Sudoku", 1, black)
        screen.blit(title_text, (500 // 2 - title_text.get_width() // 2, 100))

        # Instruction to user
        instruction_text = instruction_font.render("Choose a color:", 1, black)
        screen.blit(instruction_text, (500 // 2 - instruction_text.get_width() // 2, 190))
        
        # Buttons dimensions
        pink = pygame.Rect(100, 270, 80, 50)
        orange = pygame.Rect(210, 270, 80, 50)
        violet = pygame.Rect(305,270,80,50)
        red = pygame.Rect(100, 370, 80, 50)
        green = pygame.Rect(210, 470, 80, 50)
        yellow = pygame.Rect(205,370,80,50)
        blue = pygame.Rect(100,470,80,50)

        # Draw the buttons to screen
        pygame.draw.rect(screen, black, pink)
        pygame.draw.rect(screen, black, pygame.Rect(100, 370, 80, 50)) #red
        pygame.draw.rect(screen, black, blue)
        pygame.draw.rect(screen, black, orange)
        pygame.draw.rect(screen, black, yellow)
        pygame.draw.rect(screen, black, green)
        pygame.draw.rect(screen, black, violet)
        
        # possition and text of the buttons
        pink_text = instruction_font.render("pink", 1, white)
        screen.blit(pink_text, (120, 280))

        # possition and text of the buttons
        red_text = instruction_font.render("red", 1, white)
        screen.blit(red_text, (120, 380))

        # possition and text of the buttons
        blue_text = instruction_font.render("blue", 1, white)
        screen.blit(blue_text, (120, 480))

        # possition and text of the buttons
        orange_text = instruction_font.render("orange", 1, white)
        screen.blit(orange_text, (220, 280))

        # possition and text of the buttons
        yellow_text = instruction_font.render("yellow", 1, white)
        screen.blit(yellow_text, (220, 380))
        
        # possition and text of the buttons
        green_text = instruction_font.render("green", 1, white)
        screen.blit(green_text, (220, 480))

        # possition and text of the buttons
        violet_text = instruction_font.render("violet", 1, white)
        screen.blit(violet_text, (320, 280))

        # update screen
        pygame.display.update()
        
        # Declaring a True value for while loop
        waiting_for_start = True
        while waiting_for_start == True:
            for event in pygame.event.get():
                # listen for quit event
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                # listen for mouse position and clicks
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    if pink.collidepoint(mouse_pos):
                        print("pink")
                        self.color = pink2
                        waiting_for_start = False
                    elif red.collidepoint(mouse_pos):
                        print("red")
                        self.color = red2
                        waiting_for_start = False
                    elif blue.collidepoint(mouse_pos):
                        print("blue")
                        self.color = blue2
                        waiting_for_start = False
                    elif orange.collidepoint(mouse_pos):
                        print("orange")
                        self.color = orange2
                        waiting_for_start = False
                    elif green.collidepoint(mouse_pos):
                        print("green")
                        self.color = green2
                        waiting_for_start = False
                    elif yellow.collidepoint(mouse_pos):
                        print("yellow")
                        self.color = yellow2
                        waiting_for_start = False
                    elif violet.collidepoint(mouse_pos):
                        print("violet")
                        self.color = violet2
                        waiting_for_start = False
                    # return selected color
                    return self.color
