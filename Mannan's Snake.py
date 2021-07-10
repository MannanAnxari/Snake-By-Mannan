import pygame
import random

from pygame.constants import K_RETURN

x = pygame.init()

# Local Variables
# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
bg = (38, 47, 78, 255)
snake = (4, 184, 113, 255)
screen_Height = 600
screen_Width = 900
gameDisplay = pygame.display.set_mode((screen_Width, screen_Height))
font = pygame.font.SysFont(None, 30)

# level 2 Colors
bg1 = (45, 41, 38, 255)
snake1 = (233, 76, 61, 255)

# level 2 Colors
bg2 = (23, 74, 69, 255)
snake2 = (175, 184, 179, 255)

# level 2 Colors
bg3 = (4, 15, 79, 255)
snake3 = (245, 163, 28, 255)

# level 3 Colors
snake4 = (218, 33, 101, 255)
bg4 = (12, 17, 55, 255)


def screen_Text(text, color, x, y):
    text_screen = font.render(text, True, color)
    gameDisplay.blit(text_screen, [x, y])


def plot_snk(gameDisplay, black, snk_list, snake_size):
    for x, y in snk_list:
        pygame.draw.rect(gameDisplay, black, [x, y, snake_size, snake_size])


def ifborder():
    X = 0
    Y = 0
    width = 20
    height = screen_Height
    pygame.draw.rect(gameDisplay, snake, (X, Y, width, height))
    X = 0
    Y = 0
    width = screen_Width
    height = 20
    pygame.draw.rect(gameDisplay, snake, (X, Y, width, height))
    X = 0
    Y = screen_Height-20
    width = screen_Width
    height = 20
    pygame.draw.rect(gameDisplay, snake, (X, Y, width, height))
    X = screen_Width-20
    Y = 0
    width = 20
    height = screen_Height
    pygame.draw.rect(gameDisplay, snake, (X, Y, width, height))


def ifborderlv1():
    X = 0
    Y = 0
    width = 20
    height = screen_Height
    pygame.draw.rect(gameDisplay, snake1, (X, Y, width, height))
    X = 0
    Y = 0
    width = screen_Width
    height = 20
    pygame.draw.rect(gameDisplay, snake1, (X, Y, width, height))
    X = 0
    Y = screen_Height-20
    width = screen_Width
    height = 20
    pygame.draw.rect(gameDisplay, snake1, (X, Y, width, height))
    X = screen_Width-20
    Y = 0
    width = 20
    height = screen_Height
    pygame.draw.rect(gameDisplay, snake1, (X, Y, width, height))


def ifborderlv2():
    X = 0
    Y = 0
    width = 20
    height = screen_Height
    pygame.draw.rect(gameDisplay, snake2, (X, Y, width, height))
    X = 0
    Y = 0
    width = screen_Width
    height = 20
    pygame.draw.rect(gameDisplay, snake2, (X, Y, width, height))
    X = 0
    Y = screen_Height-20
    width = screen_Width
    height = 20
    pygame.draw.rect(gameDisplay, snake2, (X, Y, width, height))
    X = screen_Width-20
    Y = 0
    width = 20
    height = screen_Height
    pygame.draw.rect(gameDisplay, snake2, (X, Y, width, height))


def ifborderlv3():
    X = 0
    Y = 0
    width = 20
    height = screen_Height
    pygame.draw.rect(gameDisplay, snake3, (X, Y, width, height))
    X = 0
    Y = 0
    width = screen_Width
    height = 20
    pygame.draw.rect(gameDisplay, snake3, (X, Y, width, height))
    X = 0
    Y = screen_Height-20
    width = screen_Width
    height = 20
    pygame.draw.rect(gameDisplay, snake3, (X, Y, width, height))
    X = screen_Width-20
    Y = 0
    width = 20
    height = screen_Height
    pygame.draw.rect(gameDisplay, snake3, (X, Y, width, height))


def elseborder():

    # Border
    X = 0
    Y = 0
    width = 20
    height = screen_Height
    pygame.draw.rect(gameDisplay, snake4, (X, Y, width, height))

    X = 0
    Y = 0
    width = screen_Width
    height = 20
    pygame.draw.rect(gameDisplay, snake4, (X, Y, width, height))

    X = 00
    Y = screen_Height-20
    width = screen_Width
    height = 20
    pygame.draw.rect(gameDisplay, snake4, (X, Y, width, height))
    X = screen_Width-20
    Y = 00
    width = 20
    height = screen_Height
    pygame.draw.rect(gameDisplay, snake4, (X, Y, width, height))


def game_Loop():

    # Defining FPS
    fps = 20

    # Creating Snake Head
    snake_x = screen_Width/2
    snake_y = screen_Height/2
    # snake_size = 10

    # Initilize Display Size
    gameDisplay = pygame.display.set_mode((screen_Width, screen_Height))

    # Handel Exit Events
    exit_Game = False
    game_Over = False

    # Other Vars
    velocity_x = 0
    velocity_y = 0
    food_x = random.randint(30, screen_Width/2)
    food_y = random.randint(30, screen_Height/2)
    radius1 = 8
    score = 0
    snk_list = []
    snk_length = 1
    snake_size = 15

    with open("high_score.txt", "r") as f:
        high_Score = f.read()

    # Take Title
    pygame.display.set_caption("Mannan's Snake")
    pygame.display.update()

    # Creating Py Clock
    clock = pygame.time.Clock()

    # Game Loop
    while not exit_Game:

        if game_Over == True:
            with open("high_score.txt", "w") as f:
                f.write(str(high_Score))

            gameDisplay.fill(black)
            screen_Text("Game Over! Press Enter To TryAgain",
                        white, 250, 250)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_Game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == K_RETURN:
                        game_Loop()
        else:

            for event in pygame.event.get():

                # Handel Our Exit Button
                if event.type == pygame.QUIT:
                    exit_Game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = 10
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        velocity_x = -10
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        velocity_y = -10
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        velocity_y = 10
                        velocity_x = 0

                    if event.key == pygame.K_h:
                        score += 10
                        if score == high_Score or score > int(high_Score):
                            high_Score = int(high_Score) + 10

                    if event.key == pygame.K_s:
                        score -= 10
                        if score == high_Score or score > int(high_Score):
                            high_Score = int(high_Score) + 10

            snake_x += velocity_x
            snake_y += velocity_y

            if abs(snake_x - food_x) < 10 and abs(snake_y - food_y) < 13:
                score += 10
                food_x = random.randint(30, screen_Width/2)
                food_y = random.randint(30, screen_Height/2)
                snk_length += 2.5

                if score > int(high_Score):
                    high_Score = score

            if score == 0 or score < 110:

                gameDisplay.fill(bg)

                ifborder()

                screen_Text("Score : " + str(score), white, 400, 30)

                if score == int(high_Score):
                    screen_Text("High Score : " + str(high_Score),
                                snake, 370, 550)
                else:
                    screen_Text("High Score : " +
                                str(high_Score), white, 370, 550)

                pygame.draw.circle(gameDisplay, white, (
                    food_x, food_y), radius1)

                head = []
                head.append(snake_x)
                head.append(snake_y)
                snk_list.append(head)

                if len(snk_list) > snk_length:
                    del snk_list[0]

                if head in snk_list[:-1]:
                    game_Over = True

                if screen_Width < snake_x or snake_y < 0 or snake_y < 0 or snake_y > screen_Height:
                    game_Over = True

                plot_snk(gameDisplay, snake, snk_list, snake_size)

            elif score == 100 or score < 210:

                gameDisplay.fill(bg2)

                ifborderlv2()

                screen_Text("Score : " + str(score), white, 400, 30)

                if score == int(high_Score):
                    screen_Text("High Score : " + str(high_Score),
                                snake2, 370, 550)
                else:
                    screen_Text("High Score : " +
                                str(high_Score), white, 370, 550)

                pygame.draw.circle(gameDisplay, white, (
                    food_x, food_y), radius1)

                head = []
                head.append(snake_x)
                head.append(snake_y)
                snk_list.append(head)

                if len(snk_list) > snk_length:
                    del snk_list[0]

                if head in snk_list[:-1]:
                    game_Over = True

                if screen_Width < snake_x or snake_y < 0 or snake_y < 0 or snake_y > screen_Height:
                    game_Over = True

                plot_snk(gameDisplay, snake2, snk_list, snake_size)

            elif score == 200 or score < 310:

                gameDisplay.fill(bg2)

                ifborderlv3()

                screen_Text("Score : " + str(score), white, 400, 30)

                if score == int(high_Score):
                    screen_Text("High Score : " + str(high_Score),
                                snake3, 370, 550)
                else:
                    screen_Text("High Score : " +
                                str(high_Score), white, 370, 550)

                pygame.draw.circle(gameDisplay, white, (
                    food_x, food_y), radius1)

                head = []
                head.append(snake_x)
                head.append(snake_y)
                snk_list.append(head)

                if len(snk_list) > snk_length:
                    del snk_list[0]

                if head in snk_list[:-1]:
                    game_Over = True

                if screen_Width < snake_x or snake_y < 0 or snake_y < 0 or snake_y > screen_Height:
                    game_Over = True

                plot_snk(gameDisplay, snake3, snk_list, snake_size)

            elif score == 300 or score < 410:
                gameDisplay.fill(bg1)

                ifborderlv1()

                screen_Text("Score : " + str(score), white, 400, 30)

                if score == int(high_Score):
                    screen_Text("High Score : " + str(high_Score),
                                snake1, 370, 550)
                else:
                    screen_Text("High Score : " +
                                str(high_Score), white, 370, 550)

                pygame.draw.circle(gameDisplay, white, (
                    food_x, food_y), radius1)

                head = []
                head.append(snake_x)
                head.append(snake_y)
                snk_list.append(head)

                if len(snk_list) > snk_length:
                    del snk_list[0]

                if head in snk_list[:-1]:
                    game_Over = True

                wid = 20
                if screen_Width+wid < snake_x or snake_x < wid or snake_y+wid < wid or snake_y > screen_Height+wid:
                    game_Over = True

                plot_snk(gameDisplay, snake1, snk_list, snake_size)

            elif score == 400 or score < 500:
                gameDisplay.fill(bg3)

                ifborderlv3()

                screen_Text("Score : " + str(score), white, 400, 30)

                if score == int(high_Score):
                    screen_Text("High Score : " + str(high_Score),
                                snake3, 370, 550)
                else:
                    screen_Text("High Score : " +
                                str(high_Score), white, 370, 550)

                pygame.draw.circle(gameDisplay, white, (
                    food_x, food_y), radius1)

                head = []
                head.append(snake_x)
                head.append(snake_y)
                snk_list.append(head)

                if len(snk_list) > snk_length:
                    del snk_list[0]

                if head in snk_list[:-1]:
                    game_Over = True

                wid = 20
                if screen_Width+wid < snake_x or snake_x < wid or snake_y+wid < wid or snake_y > screen_Height+wid:
                    game_Over = True

                plot_snk(gameDisplay, snake3, snk_list, snake_size)

            else:
                gameDisplay.fill(bg4)

                elseborder()

                screen_Text("Score : " + str(score), white, 400, 30)

                if score == int(high_Score):
                    screen_Text("High Score : " + str(high_Score),
                                snake4, 370, 550)
                else:
                    screen_Text("High Score : " +
                                str(high_Score), white, 370, 550)

                pygame.draw.circle(gameDisplay, white, (
                    food_x, food_y), radius1)

                head = []
                head.append(snake_x)
                head.append(snake_y)
                snk_list.append(head)

                if len(snk_list) > snk_length:
                    del snk_list[0]

                if head in snk_list[:-1]:
                    game_Over = True

                wid = 20
                if screen_Width+wid < snake_x or snake_x < wid or snake_y+wid < wid or snake_y > screen_Height+wid:
                    game_Over = True

                plot_snk(gameDisplay, snake4, snk_list, snake_size)

        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()


game_Loop()
