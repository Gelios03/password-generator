import random

DIGITS = '0123456789'
UPPERCASE = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LOWERCASE = 'abcdefghijklmnopqrstuvwxyz'
SYMBOLS = '!#$%&*+-=?@^_'
AMBIGUOUS = 'il1Lo0O'

chars = ''

num_passwords = int(input('Количество паролей: '))
length_password = int(input('Длина пароля: '))
include_digits = input('Включать цифры? (да / нет) ')
include_uppercase = input('Включать прописные буквы? (да / нет) ')
include_lowercase = input('Включать строчные буквы? (да / нет) ')
include_symbols = input('Включать символы? (да / нет) ')
include_ambiguous = input('Исключить неоднозначные символы: «il1Lo0O»? (да / нет) ')