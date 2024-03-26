import json
from files import JSON_FILE_PATH
from csv import DictReader
from files import CSV_FILE_PATH

with open(JSON_FILE_PATH, "r") as f:
    users = json.load(f)

    Lst = []
    for user in users:
        dict_short = dict()
        dict_short['name'] = user['name']
        dict_short['gender'] = user['gender']
        dict_short['address'] = user['address']
        dict_short['age'] = user['age']
        Lst.append(dict_short)

with open(CSV_FILE_PATH, newline='') as f:
    books_reader = DictReader(f)

    books = []
    for item in books_reader:
        dict_books = dict()
        dict_books['title'] = item['Title']
        dict_books['author'] = item['Author']
        dict_books['pages'] = item['Pages']
        dict_books['genre'] = item['Genre']
        books.append(dict_books)

while books:
    for user in Lst:
        it = iter(books)
        try:
            one_book = next(it)
            user['book'] = one_book
            del one_book
            print(user)
        except StopIteration:
            print('Iteration is over')

# with open("result.json", "w") as f:
#     s = json.dumps(Lst, indent=4)
#     f.write(s)
