import random

print("Добро пожаловать в числовую угадайку")
print("Введите первое число")
num1= int(input())
print("Введите второе число")
num2 = int(input())

def is_valid(number):
    return number.isdigit() and num1 <= int(number) <= num2 

number = random.randint(num1, num2)

game_flag = "да"
guess_count = 0

print(f"Загадайте число от {num1} до {num2}")
while game_flag.lower() == "да":    
    num = input()
    if is_valid(num):
        num = int(num)
        if num < number:
            guess_count += 1
            print("Ваше число меньше загаданного, попробуйте еще разок")
        elif num > number:
            guess_count += 1
            print("Ваше число больше загаданного, попробуйте еще разок")
        elif num == number:
            print("Вы угадали, поздравляем!")
            print(f"Ваше количество попыток: {guess_count}")
            
    else:
        print("А может быть все-таки введем число от 1 до 100?")

    print("Хотите продолжить? да, нет")
    game_flag = input()
    if game_flag == "да":
        print("Погнали еще...")

print("Спасибо, что сыграли в числовую угадайку, еще увидимся!")