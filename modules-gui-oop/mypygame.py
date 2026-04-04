import pygame
import random

pygame.init()

# setting the screen
screen = pygame.display.set_mode((500, 300))
pygame.display.set_caption('game py')
# frame rates
clock = pygame.time.Clock()
dt = 0

class Player:
    # defalt values
    def __init__(self, x, y):
        self.pos = pygame.Vector2(x, y)
        self.start_pos = pygame.Vector2(x, y)

    # print the player position
    def get_position(self):
        print(f'x: {self.pos.x}, y: {self.pos.y}')

    # leads the player movement and checks the position to limit
    def move_player(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a] and keys[pygame.K_SPACE]:
            self.pos.x -= 500 * dt
        elif keys[pygame.K_d] and keys[pygame.K_SPACE]:
            self.pos.x += 500 * dt
        elif keys[pygame.K_a]:
            self.pos.x -= 360 * dt
        elif keys[pygame.K_d]:
            self.pos.x += 360 * dt
        else:
            self.get_position()

        if self.pos.x < 0:
            self.pos.x = 0
        elif self.pos.x > screen.get_width() - 40:
            self.pos.x = screen.get_width() - 40

    # setting the player
    def draw_player(self, surface):
        rect = pygame.Rect(self.pos.x, self.pos.y, 40, 40)
        pygame.draw.rect(surface, 'green', (self.pos.x, self.pos.y, 40, 40))
        return rect

class Obstacle:
    # default values
    def __init__(self, x, y):
        self.pos = pygame.Vector2(x, y)

    # falling function || checks the position to reset
    def fall(self, dt):
        self.pos.y += 400 * dt

        if self.pos.y > screen.get_height():
            self.pos.y = random.randint(-90, -40)
            self.pos.x = random.randint(0, screen.get_width() - 40)

    # setting the obstacle
    def draw_obstacle(self, surface):
        rect = pygame.Rect(self.pos.x, self.pos.y, 40, 40)
        pygame.draw.rect(surface, 'grey', (self.pos.x, self.pos.y, 40, 40))
        return rect


player = Player(screen.get_width() / 2, screen.get_height() / 2)
obstacles = [Obstacle(random.randint(0, 460), -40) for _ in range(3)]

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    player_rect = player.draw_player(screen)
    player.move_player(dt)
    for obstacle in obstacles:
        obstacle.fall(dt)
        obstacle_rect = obstacle.draw_obstacle(screen)

        if player_rect.colliderect(obstacle_rect):
            print("Game over!") 
            running = False

    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()

