# dvd_image_moving.py
# create a rectangle that moves around the screen

# GOALS:
#   * draw a rectangle on the screen
#   * move the rectangle in x and y
#   * create a rectangle class
#       * size and position
#       * colour
#       * velocity x- and y- direction


import pygame

# ----- CONSTANTS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
SKY_BLUE = (95, 165, 228)
WIDTH = 800
HEIGHT = 600
TITLE = "DVD Screensaver"

class Rectangle:
    def __init__(self, colour=WHITE):
        self.width, self.height = (150, 80)
        self.x, self.y = (WIDTH / 2, HEIGHT / 2)

        self.colour = colour

        self.vel_x = 3

    def draw(self, screen):
        pygame.draw.rect(
            screen,
            self.colour,
            [
                self.x,
                self.y,
                self.width,
                self.height
            ]
        )



def main():
    pygame.init()

    # ----- SCREEN PROPERTIES
    size = (WIDTH, HEIGHT)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption(TITLE)

    # ----- LOCAL VARIABLES
    done = False
    clock = pygame.time.Clock()

    block_one = Rectangle((0, 255, 0))



    # ----- MAIN LOOP
    while not done:
        # -- Event Handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # ----- LOGIC

        # ----- DRAW
        screen.fill(BLACK)
        black_one.draw(screen)

        # ----- UPDATE
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()