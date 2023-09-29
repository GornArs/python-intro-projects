from pynput import keyboard
from random import randint
import time as t
import os

clear = lambda: os.system('cls')
clear()
# Ввод переменных
inv = False
appletaken = False
WIDTH, HEIGHT = 12, 12
do = True
colcount = 0
direction = (1, 0)
applecount = 0


# Случайная позиция
def random_position():
    return randint(0, HEIGHT - 1), randint(0, WIDTH - 1)


# Фиксирование клваиш
def process_press(key):
    # обработчик нажатия на клавиши (можно сделать и поаккуратнее)
    global direction
    match key:
        case keyboard.Key.left:
            direction = (-1, 0)
        case keyboard.Key.up:
            direction = (0, -1)
        case keyboard.Key.right:
            direction = (1, 0)
        case keyboard.Key.down:
            direction = (0, 1)


# Генерация объектов
def snake_gen():
    snake = [random_position()]
    return snake


def apple_gen():
    apple = random_position()
    return apple


def collisa_check(apple, snake):
    while apple in snake:
        apple = random_position()
    return apple


snake = snake_gen()
apple = apple_gen()
apple = collisa_check(apple, snake)


def drawfield():
    print("%%%%%%%%%%%%%")
    for h in range(HEIGHT):
        for w in range(WIDTH):
            ne = False
            # Отриса змейки
            for s in range(len(snake)):
                if w == snake[s][0] and h == snake[s][1]:
                    if s==0:
                        print("()", end=" ")
                        ne = True
                    else:
                        print("OO", end=" ")
                        ne = True
            # Яблоко
            if w == apple[0] and h == apple[1]:
                print("AP", end=" ")
                ne = True
            if not ne:
                print("__", end=" ")
        print()
    print("%%%%%%%%%%%%%")


def eat(appletaken, inv):
    if appletaken == False: inv = False
    appletaken = False
    return appletaken, inv


# Проверка на яблоко
def eaten_apple(apple, appletaken, inv, alc):
    while apple in snake:
        snake.append(snake[-1])
        apple = random_position()
        appletaken = True
        inv = True
        alc += 1
    return apple, appletaken, inv, alc


def movement(direction, snake, WIDTH, HEIGHT):
    head = snake[0]
    snake1 = [snake[-1]] + snake[:-1]
    snake1[0] = (head[0] + direction[0], head[1] + direction[1])
    snake = snake1
    if snake1[0][0] < 0:
        snake1[0] = (WIDTH - 1, snake1[0][1])
    elif snake1[0][0] > WIDTH - 1:
        snake1[0] = (0, snake1[0][1])
    if snake1[0][1] < 0:
        snake1[0] = (snake1[0][0], HEIGHT - 1)
    elif snake1[0][1] > HEIGHT - 1:
        snake1[0] = (snake1[0][0], 0)

    snake = snake1
    return head, snake


def collision(snake, cc):
    inl = True
    col = False
    for i in range(len(snake)):
        if snake.count(snake[i]) != 1:
            col = True
    if col:
        print("Collision!")
        cc += 1
        col = False
        if cc >= 2:
            print("Collision")
            inl = False
    else:
        if cc <= 0:
            cc = 0
        else:
            cc -= 1

    return inl, cc


# оно умеет мониторить нажатия на кнопки!
with keyboard.Listener(on_press=process_press) as listener:
    while do:
        # Вывод
        drawfield()

        # Поглощение яблока
        appletaken, inv = eat(appletaken, inv)
        # Проверка на яблоко
        apple, appletaken, inv, applecount = eaten_apple(apple, appletaken, inv, applecount)

        # Мувмент

        head, snake = movement(direction, snake, WIDTH, HEIGHT)

        do, colcount = collision(snake, colcount)

        t.sleep(0.2)
        clear()
        pass
print("You lose!")
u=input()