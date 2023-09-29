import random as r
import dicti
import os

cycle = True
anslist = []


def get_indices(lst, el):
    return [i for i in range(len(lst)) if lst[i] == el]


def keyword():
    return dicti.spl[r.randint(0, int(len(dicti.spl)) - 1)]


def secret(a):
    return str(len(a) * "_")


def tries(a):
    x = int(len(a) * 2)
    if x >= 30: x = 25
    return x


def infoprint(tries, secretw):
    print("Hangman")
    print("Amount of tries:", tries)
    print(*list(secretw))
    print("Enter your guess..")


def anstake(listofans):
    rep = True
    while rep:
        g = str(input())
        if g not in listofans:
            listofans.append(g)
            rep = False
        else:
            print("You have already given this answer!")
    return g


def indexes(word, answer):
    indexlist = get_indices(word, answer)
    if word[0] == answer: indexlist = [0] + indexlist
    return indexlist


def rightwrong(indexlist, tramo, sword, el):
    if len(indexlist) == 0:
        print("MISTAKE")
        tramo -= 1
    else:
        print("RIGHT")
        for i in range(len(list(indexlist))):
            sword = list(sword)
            sword[indexlist[i]] = el

    return tramo, sword


def winlose(word, sword, log, tri):
    if get_indices(sword, "_") == []:
        print("----WIN!----")
        log = False
    elif tri == 0:
        print("----LOSE!----")
        log = False
        print("THE WORD IS:", word)
    return log


if __name__ == "__main__":

    clear = lambda: os.system('cls')
    clear()
    # Перед циклом
    word = keyword()
    sword = secret(word)
    amotry = tries(word)

    while cycle:
        infoprint(amotry, sword)
        answer = anstake(anslist)
        indexlist = indexes(word, answer)
        amotry, sword = rightwrong(indexlist, amotry, sword, answer)
        cycle = winlose(word, sword, cycle, amotry)
