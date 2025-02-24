import random

def generate_password(chars, length):
    res = ""
    for _ in range(length):
        res += random.choice(chars)

    return res

digits = "0123456789"
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
punctuation = "!#$%&*+-=?@^_"
bad_letters = "il1Lo0O"

chars = ""
print("Введите количество паролей для генерации")
password_quantity = int(input())
print("Введите длину пароля")
password_length = int(input())
print("Включать ли цифры в пароль?, (y or n)")
is_digit = input()
print("Включать ли маленькие символы?, (y or n)")
is_lower = input()
print("Включать ли большие символы?, (y or n)")
is_upper = input()
print("Включать ли пунктуационные символы?, (y or n)")
is_punct = input()
print("Включать ли плохие символы?, (y or n)")
is_bad = input()

if is_digit == "y":
    chars += digits
if is_lower == "y":
    chars += lowercase_letters
if is_upper == "y":
    chars += uppercase_letters
if is_punct == "y":
    chars += punctuation
if is_bad == "y":
    chars += bad_letters

for _ in range(password_quantity):
    print(generate_password(chars, password_length))