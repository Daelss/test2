import random

player = input("Выберите: камень, ножницы или бумага: ")

bot = ["камень", "бумага", "ножницы"]
bot_action = random.choice(bot)

if player != bot:
    print("Вы ввели не то, попробуйте ещё раз")

if player == bot_action:
    print(f"Оба пользователя выбрали {player}. Ничья!!")
elif player == "камень":
    if bot_action == "ножницы":
        print("Камень бьет ножницы! Вы победили!")
    else:
        print("Бумага оборачивает камень! Вы проиграли.")
elif player == "бумага":
    if bot_action == "камень":
        print("Бумага оборачивает камень! Вы победили!")
    else:
        print("Ножницы режут бумагу! Вы проиграли.")
elif player == "ножницы":
    if bot_action == "бумага":
        print("Ножницы режут бумагу! Вы победили!")
    else:
        print("Камень бьет ножницы! Вы проиграли.")
