
from random import randint

import controller
import model
from data_base import table_department

run_program = True

while run_program:
    t = int(input('Введите действие (1-добавить, 3-искать, 4-показать все, 5-экспорт в файл, 6-выйти): '))
    if t == 1:
        n = input('Введите ФИО: ')
        a = input('Введите табельный №: ')
        print("Выберите департамент:")
        print(table_department)
        p = input('Введите id департамента: ')
        user = model.User(randint(0, 100), n, a, int(p))
        controller.add_user_to_db(user)
    elif t == 3:
        p = input('Введите данные пользователя: ')
        results = controller.search_user_in_db(p)
        if results.__sizeof__() == 0:
            print("Такого пользователя не существует:")
        else:
            for v in results:
                print(v)
    elif t == 4:
        results = controller.get_all_users()
        for v in results:
            print(v)
    elif t == 5:
        controller.export_file()
    elif t == 6:
        run_program = False
        break
