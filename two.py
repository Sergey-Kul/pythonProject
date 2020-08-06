from random import randint
def play():
    random_int = randint (0, 100)
    while True:
        user_guess = int (input("Какой номер мы загадали (0-100):"))
        if user_guess == randint:
            print("Вы нашли номер", random_int, 'Поздравляю!')
            break
        if user_guess < random_int:
            print("Ваш номер меньше чем мы загадали.")
            continue
        if user_guess > random_int:
            print("Ваш номер больше чем мы загадали.")
            continue
if __name__== '__main__':
    play()