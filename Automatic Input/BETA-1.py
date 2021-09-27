
import random
import pprint
import time
import copy
import pygame

feldgrose = int(input("Wie gros soll das Feld sein "))

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


# Create a 2 dimensional array. A two dimensional
# array is simply a list of lists.
grid = []

# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 15
HEIGHT = 15

# This sets the margin between each cell
MARGIN = 2

# Create a 2 dimensional array. A two dimensional
# array is simply a list of lists.
grid = []
for row in range(feldgrose):
    # Add an empty array that will hold each cell
    # in this row
    grid.append([])
    for column in range(feldgrose):
        grid[row].append(0)  # Append a cell

# Initialize pygame
pygame.init()



# Set the HEIGHT and WIDTH of the screen
WINDOW_SIZE = [1200, 1200]
screen = pygame.display.set_mode(WINDOW_SIZE)

pygame.display.flip()
# Set title of screen
pygame.display.set_caption("Game of life BETA")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()
einmal = 0
# -------- Main Program Loop -----------
while einmal !=1:
    einmal = einmal +1
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
    for row in range(feldgrose):
        for column in range(feldgrose):
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
    clock.tick(5)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()


def main():
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

    feld = []
    for z in range(0, feldgrose):
        reihe = []
        for y in range(0, feldgrose):
            reihe.append(random.randint(0, 1))
        feld.append(copy.deepcopy(reihe))

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

        for z in range(0, feldgrose):
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
            for y in range(0, feldgrose):

                zelle = str(tempreihe[y])
                nachbarn = " "
                # print(z)
                if z > 0 and z < feldgrose - 1 and y > 0 and y < feldgrose - 1:
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
                elif y == feldgrose - 1 and z == feldgrose - 1:

                    nachbarn = nachbarn + str(tempreihe1[y])
                    nachbarn = nachbarn + str(tempreihe[y - 1])
                    nachbarn = nachbarn + str(tempreihe1[y - 1])
                elif z == feldgrose - 1 and y == 0:

                    nachbarn = nachbarn + str(tempreihe1[y])
                    nachbarn = nachbarn + str(tempreihe1[y + 1])
                    nachbarn = nachbarn + str(tempreihe[y + 1])

                elif z == 0 and y == feldgrose - 1:
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

        for row in range(feldgrose):
            for column in range(feldgrose):
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
