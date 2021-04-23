import numpy as np
import random
from collections import Counter
from time import time

def start():
    game = np.zeros((4, 4), np.int64)
    temp = np.where(game == 0)
    zeros = []
    for i, row in enumerate(temp[0]):
        zeros.append([row, temp[1][i]])
    choice = random.choice(zeros)
    number = random.choice([2, 4])
    game[choice[0]][choice[1]] = number
    temp = np.where(game == 0)
    zeros = []
    for i, row in enumerate(temp[0]):
        zeros.append([row, temp[1][i]])
    choice = random.choice(zeros)
    number = random.choice([2, 4])
    game[choice[0]][choice[1]] = number
    return game


def new_tiles(game, high_score, counts):
    temp = np.where(game == 0)
    zeros = []
    for i, row in enumerate(temp[0]):
        zeros.append([row, temp[1][i]])
    try:
        choice = random.choice(zeros)
        number = random.choice([2, 4])
        game[choice[0]][choice[1]] = number
        return game, False
    except:
        ##        print(counts, high_score)
        return game, True


def left(game):
    new_reward = 0
    shape = game.shape
    temp = np.where(game == 0)
    counts = Counter(temp[0])
    for row in range(shape[0]):
        if counts[row] != shape[0]:
            temp_list = []
            temp_count = 0
            for i in list(game[row]):
                if i != 0:
                    temp_list.append(i)
                if i == 0:
                    temp_count += 1
            for i in range(temp_count):
                temp_list.append(0)
            game[row] = temp_list
    for row in range(shape[0]):
        for i, col in enumerate(game[row]):
            if i + 1 > shape[1] - 1:
                break
            if game[row][i] == game[row][i + 1]:
                new_reward += game[row][i] + game[row][i + 1]
                game[row][i] = game[row][i] + game[row][i + 1]
                game[row][i + 1] = 0
    for row in range(shape[0]):
        if counts[row] != shape[0]:
            temp_list = []
            temp_count = 0
            for i in list(game[row]):
                if i != 0:
                    temp_list.append(i)
                if i == 0:
                    temp_count += 1
            for i in range(temp_count):
                temp_list.append(0)
            game[row] = temp_list
    return game, new_reward


def right(game):
    new_reward = 0
    shape = game.shape
    temp = np.where(game == 0)
    counts = Counter(temp[0])
    for row in range(shape[0]):
        if counts[row] != shape[0]:
            temp_list = []
            temp_count = 0
            for i in list(game[row]):
                if i != 0:
                    temp_list.append(i)
                if i == 0:
                    temp_count += 1
            for i in range(temp_count):
                temp_list = [0] + temp_list
            game[row] = temp_list
    for row in range(shape[0]):
        for i in range(shape[0] - 1, 0, -1):
            if game[row][i] == game[row][i - 1]:
                new_reward += game[row][i] + game[row][i - 1]
                game[row][i] = game[row][i] + game[row][i - 1]
                game[row][i - 1] = 0
    for row in range(shape[0]):
        if counts[row] != shape[0]:
            temp_list = []
            temp_count = 0
            for i in list(game[row]):
                if i != 0:
                    temp_list.append(i)
                if i == 0:
                    temp_count += 1
            for i in range(temp_count):
                temp_list = [0] + temp_list
            game[row] = temp_list
    return game, new_reward


def up(game):
    new_reward = 0
    shape = game.shape
    temp = np.where(game == 0)
    counts = Counter(temp[1])
    for col in range(shape[1]):
        if counts[col] != shape[1]:
            temp_count = 0
            temp_list = []
            for row in range(shape[0]):
                if game[row][col] != 0:
                    temp_list.append(game[row][col])
                else:
                    temp_count += 1
            for i in range(temp_count):
                temp_list.append(0)
            for row in range(shape[0]):
                game[row][col] = temp_list[row]
    for col in range(shape[1]):
        for row in range(shape[0]):
            if row + 1 > shape[0] - 1:
                break
            if game[row][col] == game[row + 1][col]:
                new_reward += game[row][col] + game[row + 1][col]
                game[row][col] = game[row][col] + game[row + 1][col]
                game[row + 1][col] = 0
    for col in range(shape[1]):
        if counts[col] != shape[1]:
            temp_count = 0
            temp_list = []
            for row in range(shape[0]):
                if game[row][col] != 0:
                    temp_list.append(game[row][col])
                else:
                    temp_count += 1
            for i in range(temp_count):
                temp_list.append(0)
            for row in range(shape[0]):
                game[row][col] = temp_list[row]
    return game, new_reward


def down(game):
    new_reward = 0
    shape = game.shape
    temp = np.where(game == 0)
    counts = Counter(temp[1])
    for col in range(shape[1]):
        if counts[col] != shape[1]:
            temp_count = 0
            temp_list = []
            for row in range(shape[0] - 1, -1, -1):
                if game[row][col] != 0:
                    temp_list.append(game[row][col])
                else:
                    temp_count += 1
            for i in range(temp_count):
                temp_list.append(0)
            temp_list = temp_list[::-1]
            for row in range(shape[0] - 1, -1, -1):
                game[row][col] = temp_list[row]
    for col in range(shape[1]):
        for row in range(shape[0] - 1, -1, -1):
            if row - 1 < 0:
                break
            if game[row][col] == game[row - 1][col]:
                new_reward += game[row][col] + game[row - 1][col]
                game[row][col] = game[row][col] + game[row - 1][col]
                game[row - 1][col] = 0
    for col in range(shape[1]):
        if counts[col] != shape[1]:
            temp_count = 0
            temp_list = []
            for row in range(shape[0] - 1, -1, -1):
                if game[row][col] != 0:
                    temp_list.append(game[row][col])
                else:
                    temp_count += 1
            for i in range(temp_count):
                temp_list.append(0)
            temp_list = temp_list[::-1]
            for row in range(shape[0] - 1, -1, -1):
                game[row][col] = temp_list[row]
    return game, new_reward


def find_best_dir(board_try, attempts):
    direction = {'DOWN': 0, 'UP': 0, 'LEFT': 0, 'RIGHT': 0}
    for dir in ['DOWN', 'UP', 'LEFT', 'RIGHT']:
        for i in range(attempts):
            # if i % 100 == 0:
            #     print(i, direction)
            available_choices = [dir]
            board = board_try.copy()
            turn = 0
            failed = False
            while not failed:
                reward = 0
                start_board = board.copy()
                temp_choice = random.choice(available_choices)
                available_choices.remove(temp_choice)
                if temp_choice == 'DOWN':
                    board, reward = down(board)
                if temp_choice == 'UP':
                    board, reward = up(board)
                if temp_choice == 'LEFT':
                    board, reward = left(board)
                if temp_choice == 'RIGHT':
                    board, reward = right(board)
                temp123 = []
                for i in [0, 1, 2, 3]:
                    for ii in [0, 1, 2, 3]:
                        temp123.append(start_board[i][ii] == board[i][ii])
                if not np.all(temp123):
                    turn += 1
                    board, failed = new_tiles(board, 0, turn)
                    available_choices = ['DOWN', 'UP', 'LEFT', 'RIGHT']
                if available_choices == []:
                    failed = True
            direction[dir] += turn
    print(sorted(direction.items(), key=lambda item: item[1], reverse=True))
    return list(dict(sorted(direction.items(), key=lambda item: item[1], reverse=True)).keys())[0]


scores = []
turns = []


for game_tries in range(1):
    board_keep = start()
    score = 0
    turn = 0
    failed = False
    while not failed:
        reward = 0
        start_board = board_keep.copy()
        temp_choice = find_best_dir(board_keep.copy(), 3000)
        if temp_choice == 'DOWN':
            board_keep, reward = down(board_keep)
        if temp_choice == 'UP':
            board_keep, reward = up(board_keep)
        if temp_choice == 'LEFT':
            board_keep, reward = left(board_keep)
        if temp_choice == 'RIGHT':
            board_keep, reward = right(board_keep)
        temp123 = []
        for i in [0, 1, 2, 3]:
            for ii in [0, 1, 2, 3]:
                temp123.append(start_board[i][ii] == board_keep[i][ii])
        score += reward
        if not np.all(temp123):
            turn += 1
            board_keep, failed = new_tiles(board_keep, score, turn)
        print(board_keep)
        print(turn, score)



# 1071 26092 @ 300
# 604 13484 @ 50
