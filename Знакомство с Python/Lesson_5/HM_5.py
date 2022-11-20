import re
import os

import candy_game
import tic_toe_game
import rle

text = """ Приветствие! Здесь будут разные слова. Слова: Один, двабвб, три . Удалится ли слово с абв ?"""
# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
def abc_clr(_text):
    words_list = re.findall(r"[\w']+|[.,!?; ]", _text)
    words_list = [word for word in words_list if "абв" not in word]
    res = "".join(words_list)
    print(res)
    print()

# print(text)
# abc_clr(text)
# os.system("pause")


# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

def try_candy_game(candies = 10, max_step=5, mode =2):
    mygame = candy_game.Game(candies, max_step, _mode = mode ) # mode: 0 - игра с игроком; 1 - игра с ботом; 2 - игра с умным ботом
    mygame.play()

# Создайте программу для игры в ""Крестики-нолики"".
def try_tic_toe():
    mygame = tic_toe_game.Game()
    mygame.play()

# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
def try_rle():
    with open("input_text.txt", "r") as input_file:
        data = input_file.read()
        zip_text = rle.encode(data)
    with open("encode_text.txt", "w") as encode_file:
        encode_file.write(zip_text)
    with open("encode_text.txt", "r") as encode_file:
        data = encode_file.read()
        unzip_text = rle.decode(data)
    with open("decode_text.txt", "w") as decode_file:
        decode_file.write(unzip_text)
        

        
        
        
    

# try_candy_game()
# os.system("pause")

# try_tic_toe()
# os.system("pause")

try_rle()
os.system("pause")



    
    



    