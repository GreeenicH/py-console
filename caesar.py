def caesar_chiper(text, oper, lang, step):
    eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    eng_upper_alphabet = eng_lower_alphabet.upper()
    rus_lower_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
    rus_upper_alphabet = rus_lower_alphabet.upper()
    res = ""
    if oper.lower() == "шифрование":
        if lang.lower() == "en":
            for letter in text:
                if letter.islower() and letter in eng_lower_alphabet:
                    n = ord(letter) + step
                    if n > ord('z'):
                        n = ord('a') + (n - ord('z') - 1)
                    res += chr(n)
                elif letter.isupper() and letter in eng_upper_alphabet:
                    n = ord(letter) + step
                    if n > ord('Z'):
                        n = ord('A') + (n - ord('Z') - 1)
                    res += chr(n)
                else:
                    res += letter

        if lang.lower() == "ru":
            for letter in text:
                if letter.islower() and letter in rus_lower_alphabet:
                    n = ord(letter) + step
                    if n > ord('я'):
                        n = ord('а') + (n - ord('я') - 1)
                    res += chr(n)
                elif letter.isupper() and letter in rus_upper_alphabet:
                    n = ord(letter) + step
                    if n > ord('Я'):
                        n = ord('А') + (n - ord('Я') - 1)
                    res += chr(n)
                else:
                    res += letter

    if oper.lower() == "дешифрование":
        if lang.lower() == "en":
            for letter in text:
                if letter.islower() and letter in eng_lower_alphabet:
                    n = ord(letter) - step
                    if n < ord('a'):
                        n = ord('z') - (ord('a') - n - 1)
                    res += chr(n)
                elif letter.isupper() and letter in eng_upper_alphabet:
                    n = ord(letter) - step
                    if n < ord('A'):
                        n = ord('Z') - (ord('A') - n - 1)
                    res += chr(n)
                else:
                    res += letter

        if lang.lower() == "ru":
            for letter in text:
                if letter.islower() and letter in rus_lower_alphabet:
                    n = ord(letter) - step
                    if n < ord('а'):
                        n = ord('я') - (ord('а') - n - 1)
                    res += chr(n)
                elif letter.isupper() and letter in rus_upper_alphabet:
                    n = ord(letter) - step
                    if n < ord('А'):
                        n = ord('Я') - (ord('А') - n - 1)
                    res += chr(n)
                else:
                    res += letter

    return res
                
print("Шифр Цезаря... Старт...")
print("Введите текст")
text = input()
print("Введите оперцию (Шифрование, Дешифрование)")
oper = input()
print("Язык алфавита (русский=ru, английский=en)")
lang = input()
print("Шаг сдвига(вправо)")
step = int(input())

print(caesar_chiper(text, oper, lang, step))