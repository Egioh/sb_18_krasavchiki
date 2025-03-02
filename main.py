meme_dict = {
            "КРИНЖ": "Что-то очень странное или стыдное",
            "ЛОЛ": "Что-то очень смешное"
            }

word = input("Введите непонятное слово (большими буквами!): ")

if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print('Ups')
