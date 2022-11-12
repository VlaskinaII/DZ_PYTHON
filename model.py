class User:

    def __init__(self, user_id: int, name: str, tabel_number: str, department_id: int):
        self.user_id = user_id
        self.name = name
        self.tabel_number = tabel_number
        self.department_id = department_id


class UserWithDepartment:

    def __init__(self, user: User, department: str):
        self.user = user
        self.department = department

    def __str__(self):
        return f'ФИО: {self.user.name} Табельный №: {self.user.tabel_number} Департамент: {self.department}'