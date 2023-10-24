import sqlite3

# Создаем подключение к базе данных SQLite и создаем таблицу для хранения данных о сотрудниках
conn = sqlite3.connect("employee.db")
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS employees (
                    id INTEGER PRIMARY KEY,
                    full_name TEXT,
                    phone_number TEXT,
                    email TEXT,
                    salary REAL
                )''')

def add_employee(full_name, phone_number, email, salary):
    # Добавление нового сотрудника
    cursor.execute("INSERT INTO employees (full_name, phone_number, email, salary) VALUES (?, ?, ?, ?)",
                   (full_name, phone_number, email, salary))
    conn.commit()

def update_employee(employee_id, full_name, phone_number, email, salary):
    # Изменение данных сотрудника
    cursor.execute("UPDATE employees SET full_name=?, phone_number=?, email=?, salary=? WHERE id=?",
                   (full_name, phone_number, email, salary, employee_id))
    conn.commit()

def delete_employee(employee_id):
    # Удаление сотрудника
    cursor.execute("DELETE FROM employees WHERE id=?", (employee_id,))
    conn.commit()

def search_employee_by_name(full_name):
    # Поиск сотрудника по ФИО
    cursor.execute("SELECT * FROM employees WHERE full_name LIKE ?", ('%' + full_name + '%',))
    return cursor.fetchall()

# функции
if __name__ == "__main__":
    while True:
        print("1. Добавить сотрудника")
        print("2. Изменить сотрудника")
        print("3. Удалить сотрудника")
        print("4. Поиск по ФИО")
        print("5. Выйти")
        
        choice = input("Выберите действие: ")
        
        if choice == '1':
            full_name = input("ФИО сотрудника: ")
            phone_number = input("Номер телефона: ")
            email = input("Адрес электронной почты: ")
            salary = float(input("Заработная плата: "))
            add_employee(full_name, phone_number, email, salary)
        elif choice == '2':
            employee_id = int(input("ID сотрудника для изменения: "))
            full_name = input("Новое ФИО сотрудника: ")
            phone_number = input("Новый номер телефона: ")
            email = input("Новый адрес электронной почты: ")
            salary = float(input("Новая заработная плата: "))
            update_employee(employee_id, full_name, phone_number, email, salary)
        elif choice == '3':
            employee_id = int(input("ID сотрудника для удаления: "))
            delete_employee(employee_id)
        elif choice == '4':
            search_name = input("Введите ФИО для поиска: ")
            results = search_employee_by_name(search_name)
            if results:
                for employee in results:
                    print(employee)
            else:
                print("Сотрудник не найден.")
        elif choice == '5':
            break

    conn.close()
