import random

def generate_password(length_password, chars):
    password = ''
    for _ in range(length_password):
        password += random.choice(chars)
    return password

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

if include_digits.lower() == 'да':
    chars += DIGITS
if include_uppercase.lower() == 'да':
    chars += UPPERCASE
if include_lowercase.lower() == 'да':
    chars += LOWERCASE
if include_symbols.lower() == 'да':
    chars += SYMBOLS
if include_ambiguous.lower() == 'да':
    for char in AMBIGUOUS:
        chars = chars.replace(char, '')

if not chars:
    print('Ошибка: требуется выбрать как минимум один тип символов!')
    exit()

print('\nСгенерированные пароли:')
for i in range(num_passwords):
    password = generate_password(length_password, chars)
    print(f'{i + 1}. {password}')