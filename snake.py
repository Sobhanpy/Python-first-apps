import pygame
from random import randint

# Initialize Pygame
pygame.init()

# Set up the game window
WINDOW_WIDTH = 700
WINDOW_HEIGHT = 700
game_window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Snake Game')

# Set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Set up the game variables
SNAKE_SIZE = 10
FOOD_SIZE = 10
FPS = 10

# Set up the font
font = pygame.font.SysFont(None, 25)

# Set up the clock
clock = pygame.time.Clock()

# Define the Snake class
class Snake:
    def __init__(self):
        self.x = WINDOW_WIDTH / 2
        self.y = WINDOW_HEIGHT / 2
        self.direction = 'right'
        self.body = [(self.x, self.y), (self.x - SNAKE_SIZE, self.y), (self.x - (2 * SNAKE_SIZE), self.y)]

    def move(self):
        # Move the snake according to its direction
        if self.direction == 'right':
            self.x += SNAKE_SIZE
        elif self.direction == 'left':
            self.x -= SNAKE_SIZE
        elif self.direction == 'up':
            self.y -= SNAKE_SIZE
        elif self.direction == 'down':
            self.y += SNAKE_SIZE

        # Add the new head to the snake's body
        self.body.insert(0, (self.x, self.y))

        # Remove the tail of the snake's body
        self.body.pop()

    def draw(self):
        # Draw the snake's body
        for segment in self.body:
            pygame.draw.rect(game_window, GREEN, (segment[0], segment[1], SNAKE_SIZE, SNAKE_SIZE))

    def eat(self, food):

        if self.x == food.x and self.y == food.y:
            # print('Test ok')
            # Add a new segment to the snake's body
            self.body.append((self.x, self.y))
            return True
        else:
            return False

# Define the Food class
class Food:
    def __init__(self):
        self.x = randint(0, WINDOW_WIDTH - FOOD_SIZE)
        self.x = self.x - (self.x % 10)
        self.y = randint(0, WINDOW_HEIGHT - FOOD_SIZE)
        self.y = self.y - (self.y % 10)
    def draw(self):
        # Draw the food
        pygame.draw.rect(game_window, RED, (self.x, self.y, FOOD_SIZE, FOOD_SIZE))

# Create the Snake and Food objects
snake = Snake()
food = Food()

# Set up the game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                snake.direction = 'right'
            elif event.key == pygame.K_LEFT:
                snake.direction = 'left'
            elif event.key == pygame.K_UP:
                snake.direction = 'up'
            elif event.key == pygame.K_DOWN:
                snake.direction = 'down'

    # Move the snake
    snake.move()

    # Check if the snake has collided with the edge of the screen
    if snake.x < 0 or snake.x > WINDOW_WIDTH - SNAKE_SIZE or snake.y < 0 or snake.y > WINDOW_HEIGHT - SNAKE_SIZE:
        pygame.quit()
        quit()

    # Check if the snake has collided with itself
    for segment in snake.body[1:]:
        if snake.x == segment[0] and snake.y == segment[1]:
            pygame.quit()
            quit()

    # Check if the snake has eaten the food
    if snake.eat(food):
        # Create a new Food object
        food = Food()

    # Draw the game objects
    game_window.fill(BLACK)
    snake.draw()
    food.draw()

    # Draw the score
    score = font.render('Score: ' + str(len(snake.body) - 3), True, WHITE)
    game_window.blit(score, (10, 10))

    # Update the display
    pygame.display.update()

    # Set the FPS
    clock.tick(FPS)