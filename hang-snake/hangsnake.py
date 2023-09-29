from pynput import keyboard
from random import randint
import time as t
import random as r
import os
import snake as s
import hang1 as h
import math as m

clear = lambda: os.system('cls')
clear()

inv = s.inv
appletaken = s.appletaken
WIDTH, HEIGHT = s.WIDTH, s.HEIGHT
do = s.do
colcount = s.colcount
direction = s.direction
applecount = s.applecount

with keyboard.Listener(on_press=s.process_press) as listener:
    while do:
        s.drawfield()
        appletaken, inv = s.eat(appletaken, inv)
        apple, appletaken, inv, applecount = s.eaten_apple(apple, appletaken, inv, applecount)
        head, snake = s.movement(s.direction, snake, s.WIDTH, s.HEIGHT)
        do, colcount = s.collision(snake, colcount)
        t.sleep(0.2)
        clear()
        pass

cycle = h.cycle
anslist = h.anslist
word = h.keyword()
sword = h.secret(word)
f = int(m.sqrt(h.tries(word)))
if f>25: f=f-m.sqrt(f)
print("You have eaten {0} apples! You earned {1} tries for hangman!".format(applecount, applecount * f))
t.sleep(3)
amotry = applecount * f

while cycle:
    h.infoprint(amotry, sword)
    answer = h.anstake(anslist)
    indexlist = h.indexes(word, answer)
    amotry, sword = h.rightwrong(indexlist, amotry, sword, answer)
    cycle = h.winlose(word, sword, cycle, amotry)
t.sleep(10)