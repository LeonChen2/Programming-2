# game

import pygame

# ----- CONSTANTS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
SKY_BLUE = (95, 165, 228)
GREEN = (0, 255, 0)
WIDTH = 800
HEIGHT = 600
TITLE = "Game"



class Rectangle:
    def __init__(self, colour=WHITE):
        self.width, self.height = (60, 10)
        self.x, self.y = (400, 550)

        self.colour = colour

        self.vel_x = 0
        self.vel_y = 0

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
    def update(self):
        """Updates the location of the block in space.
        Returns:
            None
        """
        self.x += self.vel_x
        self.y += self.vel_y

        # keep it in the screen
        if self.x + self.width > WIDTH or self.x < 0:
            self.vel_x *= 0
        if self.y + self.height > HEIGHT or self.y < 0:
            self.vel_y *= 0

    def go_left(self):
        """ Called when the user hits the left arrow. """
        self.vel_x = -3

    def go_right(self):
        """ Called when the user hits the right arrow. """
        self.vel_x = 3

    def stop(self):
        """ Called when the user lets off the keyboard. """
        self.vel_x = 0



def main():
    pygame.init()

    # ----- SCREEN PROPERTIES
    size = (WIDTH, HEIGHT)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption(TITLE)

    # ----- LOCAL VARIABLES
    done = False
    clock = pygame.time.Clock()
    Paddle = Rectangle((0, 255, 0))

    # --- player



    # ----- MAIN LOOP
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    Rectangle.go_left()
                if event.key == pygame.K_RIGHT:
                    Rectangle.go_right()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and Rectangle.vel_x < 0:
                 Rectangle.stop()
                if event.key == pygame.K_RIGHT and Rectangle.vel_x > 0:
                 Rectangle.stop()

        # -- Event Handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # ----- LOGIC
        # update
        Paddle.update()

        # ----- DRAW
        screen.fill(BLACK)
        Paddle.draw(screen)



        # ----- UPDATE
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()