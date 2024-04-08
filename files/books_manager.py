import json
from files import JSON_FILE_PATH
from csv import DictReader
from files import CSV_FILE_PATH

with open(JSON_FILE_PATH, "r") as f:
    users = json.load(f)

    users_list = []
    for user in users:
        dict_users = dict()
        dict_users['name'] = user['name']
        dict_users['gender'] = user['gender']
        dict_users['address'] = user['address']
        dict_users['age'] = user['age']
        dict_users['books'] = []
        users_list.append(dict_users)

with open(CSV_FILE_PATH, newline='') as data:
    books_reader = DictReader(data)

    books_list = []
    for item in books_reader:
        dict_books = dict()
        dict_books['title'] = item['Title']
        dict_books['author'] = item['Author']
        dict_books['pages'] = item['Pages']
        dict_books['genre'] = item['Genre']
        books_list.append(dict_books)

    i = 0
    total = len(users_list)
    it = iter(books_list)
    for row in books_list:
        users_list[i]["books"].append(next(it))
        i = i + 1
        if i == total:
            i = 0

with open("result.json", "w") as final:
    data = json.dumps(users_list, indent=4)
    final.write(data)
