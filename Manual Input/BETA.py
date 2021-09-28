import random
import pprint
import time
import copy
import pygame





def main():
    # Define some colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)

    # This sets the WIDTH and HEIGHT of each grid location
    WIDTH = 15
    HEIGHT = 15

    # This sets the margin between each cell
    MARGIN = 2

    grose = int(input("Wie groß soll das Feld sein? "))

    # Create a 2 dimensional array. A two dimensional
    # array is simply a list of lists.
    grid = []
    for row in range(grose):
        # Add an empty array that will hold each cell
        # in this row
        grid.append([])
        for column in range(grose):
            grid[row].append(0)  # Append a cell

    # Initialize pygame
    pygame.init()

    # Set the HEIGHT and WIDTH of the screen
    WINDOW_SIZE = [1200, 1200]
    screen = pygame.display.set_mode(WINDOW_SIZE)

    # Loop until the user clicks the close button.
    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    # -------- Main Program Loop -----------
    while not done:
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                done = True  # Flag that we are done so we exit this loop
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # User clicks the mouse. Get the position
                pos = pygame.mouse.get_pos()
                # Change the x/y screen coordinates to grid coordinates
                column = pos[0] // (WIDTH + MARGIN)
                row = pos[1] // (HEIGHT + MARGIN)
                # Set that location to one
                grid[row][column] = 1

        # Set the screen background
        screen.fill(BLACK)

        # Draw the grid
        for row in range(grose):
            for column in range(grose):
                color = WHITE
                if grid[row][column] == 1:
                    color = GREEN
                pygame.draw.rect(screen,
                                 color,
                                 [(MARGIN + WIDTH) * column + MARGIN,
                                  (MARGIN + HEIGHT) * row + MARGIN,
                                  WIDTH,
                                  HEIGHT])

        # Limit to 60 frames per second
        clock.tick(60)

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

    # Be IDLE friendly. If you forget this line, the program will 'hang'
    # on exit.
    pygame.quit()














    pygame.init()

    # Define some colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)

    # This sets the WIDTH and HEIGHT of each grid location
    WIDTH = 15
    HEIGHT = 15

    # This sets the margin between each cell
    MARGIN = 2

    WINDOW_SIZE = [1200, 1200]
    screen = pygame.display.set_mode(WINDOW_SIZE)

    # Set title of screen
    pygame.display.set_caption("Game of life BETA")

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    #feldgrose = int(input("Wie gros soll das Feld sein "))

    feld = copy.deepcopy(grid)


    #for x in range(0, len(feld)):
        #pprint.pprint(feld[x])

    durchgang = 0
    done = False
    while not done:
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                done = True  # Flag that we are done so we exit this loop
        durchgang = durchgang + 1
        pygame.display.flip()
        time.sleep(1)
        temp = copy.deepcopy(feld)
        ubergangfeld = []

        for z in range(0, grose):
            tempreihe = copy.deepcopy(temp[z])
            ubergangreihe = copy.deepcopy(tempreihe)
            tempreihe2 = None
            tempreihe1 = None
            # if z != 0:
            try:
                tempreihe1 = copy.deepcopy(temp[z - 1])
            except:
                #print(" ")
                lala = 0
                # if z != 8:
            try:
                tempreihe2 = copy.deepcopy(temp[z + 1])
            except:
                #print(" ")
                lala = 0
            for y in range(0, grose):

                zelle = str(tempreihe[y])
                nachbarn = " "
                # print(z)
                if z > 0 and z < grose - 1 and y > 0 and y < grose - 1:
                    nachbarn = nachbarn + str(tempreihe1[y])
                    nachbarn = nachbarn + str(tempreihe1[y + 1])
                    nachbarn = nachbarn + str(tempreihe[y + 1])
                    nachbarn = nachbarn + str(tempreihe2[y + 1])
                    nachbarn = nachbarn + str(tempreihe2[y])
                    nachbarn = nachbarn + str(tempreihe2[y - 1])
                    nachbarn = nachbarn + str(tempreihe[y - 1])
                    nachbarn = nachbarn + str(tempreihe1[y - 1])
                    # print("a")

                elif y == 0 and z == 0:

                    nachbarn = nachbarn + str(tempreihe2[y])
                    nachbarn = nachbarn + str(tempreihe2[y + 1])
                    nachbarn = nachbarn + str(tempreihe[y + 1])
                    # print("b")
                elif y == grose - 1 and z == grose - 1:

                    nachbarn = nachbarn + str(tempreihe1[y])
                    nachbarn = nachbarn + str(tempreihe[y - 1])
                    nachbarn = nachbarn + str(tempreihe1[y - 1])
                elif z == grose - 1 and y == 0:

                    nachbarn = nachbarn + str(tempreihe1[y])
                    nachbarn = nachbarn + str(tempreihe1[y + 1])
                    nachbarn = nachbarn + str(tempreihe[y + 1])

                elif z == 0 and y == grose - 1:
                    # 567
                    nachbarn = nachbarn + str(tempreihe1[y])
                    nachbarn = nachbarn + str(tempreihe2[y - 1])
                    nachbarn = nachbarn + str(tempreihe[y - 1])

                if zelle == "0" and nachbarn.count("1") == 3:
                    ubergangreihe[y] = 1
                if zelle == "1" and nachbarn.count("1") < 2:
                    ubergangreihe[y] = 0
                if zelle == "1" and nachbarn.count("1") > 3:
                    ubergangreihe[y] = 0
            ubergangfeld.append(ubergangreihe)

        #print("DUCHGANG " + str(durchgang))

        #for l in range(0, len(ubergangfeld)):
         #   pprint.pprint(ubergangfeld[l])

        feld = copy.deepcopy(ubergangfeld)
        grid = copy.deepcopy(ubergangfeld)
        screen.fill(BLACK)

        for row in range(grose):
            for column in range(grose):
                color = WHITE
                if grid[row][column] == 1:
                    color = GREEN
                pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])
        clock = pygame.time.Clock()

pygame.quit()

if __name__ == '__main__':
    main()
