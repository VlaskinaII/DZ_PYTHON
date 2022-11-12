from typing import cast

from data_base import table_user, table_department
from model import User, UserWithDepartment


def add_user_to_db(user: User):
    table_user[user.user_id] = user


def get_all_users():
    results = list()
    for v in table_user.values():
        results.append(get_user(v))
    return results


def get_user(user: object):
    user = cast(User, user)
    dep = table_department.get(user.department_id)
    return UserWithDepartment(user, dep)


def search_user_in_db(text: str):
    results = list()
    for v in table_user.values():
        result = get_user(v)
        if result.user.name.__contains__(text) \
                or result.user.tabel_number.__contains__(text) \
                or result.department.__contains__(text):
            results.append(result)
    return results


def export_file():
    ss = ""
    for v in get_all_users():
        ss = ss + str(v) + '\n'
    with open(file='file_HW_8.txt', mode='w+', encoding='utf-8') as data:
        data.write(ss)
