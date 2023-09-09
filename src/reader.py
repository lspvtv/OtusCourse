import csv
import json
from src import get_path

# Считываем данные из CSV и JSON файлов
books_file = get_path('books.csv')
with open(books_file, 'r') as f:
    books = list(csv.DictReader(f))

users_file = get_path('users.json')
with open(users_file, 'r') as f:
    users = json.load(f)

# Считываем количество книг и пользователей
num_books = len(books)
num_users = len(users)

# Рассчитываем сколько книг достанется каждому
books_per_user = num_books // num_users
remainder = num_books % num_users

result = []
book_index = 0
for user in users:
    user['books'] = []

    for i in range(books_per_user):
        user['books'].append(books[book_index])
        book_index += 1

    if remainder > 0:
        user['books'].append(books[book_index])
        remainder -= 1
        book_index += 1

    result.append(user)

# Записываем результат в JSON файл
with open('result.json', 'w') as f:
    json.dump(result, f)
