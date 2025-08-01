def get_cats_info(path):
    list_of_cats = []

    try:
        with open(path, 'r', encoding="UTF-8") as file:
            cats = file.readlines()
            cats_info = [cat.strip().split(",") for cat in cats if cat.strip()]
            for index in cats_info:
                list_of_cats.append(dict(id=index[0], name=index[1], age=index[2]))
            return list_of_cats

    except FileNotFoundError:
        return "Файл не знайдено"

cats_info = get_cats_info("cats_info_file.txt")
print(cats_info)