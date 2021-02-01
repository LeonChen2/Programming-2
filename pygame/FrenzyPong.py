# Frenzy Pong
import pygame
import random

# ----- CONSTANTS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
SKY_BLUE = (95, 165, 228)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
WIDTH = 800
HEIGHT = 600
NUM_ROWS = 5
TITLE = "Frenzy Pong"

class Rectangle(pygame.sprite.Sprite):
    def __init__(self, colour=GREEN):
        super().__init__()
        self.colour = colour
        self.image = pygame.Surface([60, 10])
        self.rect = self.image.get_rect()
        self.width, self.height = (60, 10)
        self.rect.x, self.rect.y = (400, 550)
        self.image.fill(colour)
        self.vel_x = 0
        self.vel_y = 0

    def update(self):
        """Updates the location of the block in space.
        Returns:
            None
        """
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

        # keep it in the screen
        if self.rect.x + self.width > WIDTH or self.rect.x < 0:
            self.vel_x *= 0
        if self.rect.y + self.height > HEIGHT or self.rect.y < 0:
            self.vel_y *= 0

    def go_left(self):
        """ Called when the user hits the left arrow. """
        self.vel_x = -5

    def go_right(self):
        """ Called when the user hits the right arrow. """
        self.vel_x = 5

    def stop(self):
        """ Called when the user lets off the keyboard. """
        self.vel_x = 0

class Enemy(pygame.sprite.Sprite):
    def __init__(self, colour=RED):
        super().__init__()
        self.colour = colour
        self.image = pygame.Surface([60, 30])
        self.image.fill(colour)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = (400, 200)
        self.vel_x = 0
        self.vel_y = 0

    def update(self):
        if self.rect.x + self.rect.width > WIDTH or self.rect.x < 0:
            self.vel_x *= 0
        if self.rect.y + self.rect.height > HEIGHT or self.rect.y < 0:
            self.vel_y *= 0

class Ball(pygame.sprite.Sprite):
    def __init__(self, colour=YELLOW):
        super().__init__()
        self.image = pygame.Surface((10, 10))
        pygame.draw.circle(self.image, (255, 255, 0), (5, 5), 5, 10)
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 300
        self.vel_x = 3
        self.vel_y = 3

    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y
        if self.rect.right > WIDTH or self.rect.x < 0:
            self.vel_x *= -1
        if self.rect.y < 0:
            self.vel_y *= -1

        print(self.rect.x, self.rect.y)

def main():
    pygame.init()

    # ----- SCREEN PROPERTIES
    size = (WIDTH, HEIGHT)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption(TITLE)

    # ----- LOCAL VARIABLES
    done = False
    clock = pygame.time.Clock()

    # --- sprite groups
    all_sprites_group = pygame.sprite.Group()
    ball_sprites = pygame.sprite.Group()
    enemy_sprites = pygame.sprite.Group()
    rectangle_sprites = pygame.sprite.Group()

    rectangle = Rectangle()
    all_sprites_group.add(rectangle)
    rectangle_sprites.add(rectangle)

    ball = Ball()
    all_sprites_group.add(ball)
    ball_sprites.add(ball)

    enemy = Enemy()
    all_sprites_group.add(enemy)
    enemy_sprites.add(enemy)

    # ----- MAIN LOOP
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    rectangle.go_left()
                if event.key == pygame.K_RIGHT:
                    rectangle.go_right()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and rectangle.vel_x < 0:
                 rectangle.stop()
                if event.key == pygame.K_RIGHT and rectangle.vel_x > 0:
                 rectangle.stop()

        for i in range(NUM_ROWS):
            enemy = Enemy(100 + i * 20)
            enemy.rect.x = enemy.rect.x - random.choice([-10, 10])

        # -- Event Handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # ----- LOGIC

        # Player collision
        # Check for collision
        enemy_hit_group = pygame.sprite.spritecollide(ball, rectangle_sprites, False)

        # If collided, adjust the ball velocity
        if enemy_hit_group:
            ball.vel_y *= -1

        # Enemy collision
        enemy_hit_group = pygame.sprite.spritecollide(ball, enemy_sprites, True)
        if enemy_hit_group:
            ball.vel_y *= -1

        # ----- DRAW
        screen.fill(BLACK)
        all_sprites_group.draw(screen)

        # ----- UPDATE
        all_sprites_group.update()
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()

if __name__ == "__main__":
    main()
