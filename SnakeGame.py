import pygame
import random
import os

pygame.mixer.init()

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)

screen_width = 900
scree_height = 600

gameWindow = pygame.display.set_mode((screen_width, scree_height))
bgimg3 = pygame.image.load("gameover img.jpg")
bgimg3 = pygame.transform.scale(bgimg3, (screen_width, scree_height)).convert_alpha()
bgimg2 = pygame.image.load("wp2409719.jpg")
bgimg2 = pygame.transform.scale(bgimg2, (screen_width, scree_height)).convert_alpha()
bgimg = pygame.image.load("background game.jpg")
bgimg = pygame.transform.scale(bgimg, (screen_width, scree_height)).convert_alpha()
pygame.display.set_caption("Snakes ")
pygame.display.update()

# Game Specific variables

clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 55)


def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x, y])


def plot_snake(gameWindow, color, snk_list, snake_size):
    for x, y in snk_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])


def welcome():
    exit_game = False
    while not exit_game:
        if not os.path.exists("h.txt"):
            with open("h.txt", 'w') as f:
                f.write('0')
        hiscore1 = open("h.txt")
        gameWindow.fill(white)
        gameWindow.blit(bgimg2, (0, 0))
        # text_screen("Welcome To Snakes", red, 240, 260)
        # text_screen("Press Spacebar To Play",red, 210, 300 )
        # text_screen("HIGHSCORE : "+ hiscore1.read(), red , 240, 330)
        hiscore1.close()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    pygame.mixer.music.load('nagin-1-52571.mp3')
                    # pygame.mixer.music.play()
                    pygame.mixer.music.play(-1)
                    gameloop()

        pygame.display.update()
        clock.tick(60)


# GAme Loop
def gameloop():
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    snake_size = 30
    fps = 60
    food_x = random.randint(20, screen_width - 80)
    food_y = random.randint(20, scree_height - 80)
    score = 0
    velocity_y = 0
    velocity_x = 0
    init_velocity = 5
    snk_list = []
    snk_length = 1

    with open("h.txt", 'r') as f:
        hiscore = f.read()
    while not exit_game:
        if game_over:
            with open("h.txt", 'w') as f:
                f.write(str(hiscore))
            gameWindow.fill(white)
            gameWindow.blit(bgimg3, (0, 0))
            text_screen("SCORE : " + str(score), red, 250, 100)

            pygame.display.update()
            for event in pygame.event.get():
                # print(event)
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()
        else:
            for event in pygame.event.get():
                # print(event)
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0
                    if event.key == pygame.K_LEFT:
                        velocity_x = - init_velocity
                        velocity_y = 0
                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0
                    if event.key == pygame.K_UP:
                        velocity_y = - init_velocity
                        velocity_x = 0

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x - food_x) < 15 and abs(snake_y - food_y) < 15:
                # pygame.mixer.music.load('nagin-1-52571.mp3')
                # pygame.mixer.music.load('hiss.mp3')

                # pygame.mixer.music.play()
                score = score + 10
                # print("Score: ", score)

                food_x = random.randint(20, screen_width - 80)
                food_y = random.randint(20, scree_height - 80)
                snk_length += 5
                if score > int(hiscore):
                    hiscore = score

            gameWindow.fill(white)
            gameWindow.blit(bgimg, (0, 0))
            text_screen("Score: " + str(score) + "                                      HighScore : " + str(hiscore),
                        white, 5, 5)
            pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list) > snk_length:
                del snk_list[0]

            if head in snk_list[:- 1]:
                game_over = True
                pygame.mixer.music.load('gameover.wav')
                pygame.mixer.music.play()

            # pygame.draw.rect(gameWindow, black, [snake_x, snake_y, snake_size, snake_size])
            if snake_x < 0 or snake_x > screen_width or snake_y < 0 or snake_y > scree_height:
                game_over = True

                pygame.mixer.music.load('gameover.wav')
                pygame.mixer.music.play()
                # print(game_over)
            plot_snake(gameWindow, black, snk_list, snake_size)

        pygame.display.update()
        clock.tick(fps)
    pygame.quit()
    quit()


welcome()
