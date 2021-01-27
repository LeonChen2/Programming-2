# game


import pygame

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
TITLE = "Game"



class Rectangle(pygame.sprite.Sprite):
    def __init__(self, colour=GREEN):
        super().__init__()
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
        self.width, self.height = (60, 30)
        self.x, self.y = (400, 200)

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
        if self.x + self.width > WIDTH or self.x < 0:
            self.vel_x *= 0
        if self.y + self.height > HEIGHT or self.y < 0:
            self.vel_y *= 0
            
class Ball(pygame.sprite.Sprite):
    def __init__(self, colour=YELLOW):
        super().__init__()
        self.image = pygame.Surface((10, 10))
        pygame.draw.circle(self.image, (255, 255, 0), (5, 5), 5, 10)
#         self.radius, self.width = (5, 10)
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 300
        self.vel_x = 3
        self.vel_y = 3
    
    def drawCircle(self, screen):
        pygame.draw.circle(screen, (255, 255, 0), (400, 300), 5, 10)
        
    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y
        
        if self.rect.right > WIDTH or self.rect.x < 0:
            self.vel_x *= -1
        if self.rect.y < 0:
            self.vel_y *= -1
            
        #ball_hit_list = pygame.sprite.spritecollide(self, self.rect.rectangle, False)
        #for ball in ball_hit_list:
           # if self.vel_y > 0:
           #     self.rect.bottom = ball.rect.top
           #     self.vel_y *= -1
           # elif self.vel_y < 0:
           #     self.rect.top = ball.rect.bottom
            
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

    # --- enemies
    #for i in range(NUM_ROWS):
        #enemy = Enemy(100+i*20)
        #enemy.rect.x = enemy.rect.x - random.choice([-10, 10])

    # --- player
    rectangle = Rectangle()
    enemy = Enemy()
    ball = Ball()
    
    all_sprites_group = pygame.sprite.Group()
    all_sprites_group.add(ball)

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

        # -- Event Handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # ----- LOGIC



        # update
        rectangle.update()
        enemy.update()
#         ball.update()
        all_sprites_group.update()

        # ----- DRAW
        screen.fill(BLACK)
        rectangle.draw(screen)
        enemy.draw(screen)
#         ball.drawCircle(screen)
        all_sprites_group.draw(screen)

        # ----- UPDATE
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
