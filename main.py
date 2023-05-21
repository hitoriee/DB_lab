import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector

def add_teacher():
    def save_teacher():
        surname = surname_entry.get()
        name = name_entry.get()
        patronymic = patronymic_entry.get()
        birthdate = birthdate_entry.get()
        department_id = department_id_entry.get()
        position = position_entry.get()
        course = course_entry.get()
        phone = phone_entry.get()

        # Проверка на пустые значения обязательных полей
        if not surname or not name or not department_id:
            messagebox.showerror("Помилка!", "Будь ласка, заповніть обов'язкові поля: Прізвище, Ім'я, ID кафедри")
            return

        # Вставляем нового преподавателя в базу данных
        cursor = conn.cursor()
        query = "INSERT INTO викладачі (прізвище, імя, по_батькові, дата_народження, idкафедри, посада, курс, телефон) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"

        # Проверяем, есть ли значение в поле "Дата рождения"
        if not birthdate:
            birthdate = None

        values = (surname, name, patronymic, birthdate, department_id, position, course, phone)
        cursor.execute(query, values)
        conn.commit()

        teacher_window.destroy()

        refresh_treeview()

        messagebox.showinfo("Успіх!", "Новий викладач успішно доданий.")

    teacher_window = tk.Toplevel(root)
    teacher_window.title("Додати викладача")


    name_label = tk.Label(teacher_window, text="Прізвище:")
    name_label.grid(row=0, column=0, padx=5, pady=5)
    name_entry = tk.Entry(teacher_window)
    name_entry.grid(row=0, column=1, padx=5, pady=5)

    surname_label = tk.Label(teacher_window, text="Ім'я:")
    surname_label.grid(row=1, column=0, padx=5, pady=5)
    surname_entry = tk.Entry(teacher_window)
    surname_entry.grid(row=1, column=1, padx=5, pady=5)

    patronymic_label = tk.Label(teacher_window, text="По-батькові:")
    patronymic_label.grid(row=2, column=0, padx=5, pady=5)
    patronymic_entry = tk.Entry(teacher_window)
    patronymic_entry.grid(row=2, column=1, padx=5, pady=5)

    birthdate_label = tk.Label(teacher_window, text="Дата народження:")
    birthdate_label.grid(row=3, column=0, padx=5, pady=5)
    birthdate_entry = tk.Entry(teacher_window)
    birthdate_entry.grid(row=3, column=1, padx=5, pady=5)

    department_id_label = tk.Label(teacher_window, text="ID кафедри:")
    department_id_label.grid(row=4, column=0, padx=5, pady=5)
    department_id_entry = tk.Entry(teacher_window)
    department_id_entry.grid(row=4, column=1, padx=5, pady=5)

    position_label = tk.Label(teacher_window, text="Посада:")
    position_label.grid(row=5, column=0, padx=5, pady=5)
    position_entry = tk.Entry(teacher_window)
    position_entry.grid(row=5, column=1, padx=5, pady=5)

    course_label = tk.Label(teacher_window, text="Курс:")
    course_label.grid(row=6, column=0, padx=5, pady=5)
    course_entry = tk.Entry(teacher_window)
    course_entry.grid(row=6, column=1, padx=5, pady=5)

    phone_label = tk.Label(teacher_window, text="Телефон:")
    phone_label.grid(row=7, column=0, padx=5, pady=5)
    phone_entry = tk.Entry(teacher_window)
    phone_entry.grid(row=7, column=1, padx=5, pady=5)

    save_button = tk.Button(teacher_window, text="Зберегти", command=save_teacher)
    save_button.grid(row=8, columnspan=2, padx=5, pady=10)

def refresh_treeview():
    tree.delete(*tree.get_children())

    # Отримуємо дані з бази даних
    cursor = conn.cursor()
    cursor.execute("SELECT idвикладачі, прізвище, імя, по_батькові, дата_народження, idкафедри, посада, курс, телефон FROM викладачі")
    rows = cursor.fetchall()

    for row in rows:
        tree.insert("", "end", text=row[0], values=(row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]))

def edit_teacher():
    def save_edited_teacher():
        surname = surname_entry.get()
        name = name_entry.get()
        patronymic = patronymic_entry.get()
        birthdate = birthdate_entry.get()
        department_id = department_id_entry.get()
        position = position_entry.get()
        course = course_entry.get()
        phone = phone_entry.get()

        # Оновлюємо дані викладача в базі даних
        cursor = conn.cursor()
        update_query = "UPDATE викладачі SET прізвище = %s, імя = %s, по_батькові = %s, дата_народження = %s, idкафедри = %s, посада = %s, курс = %s, телефон = %s WHERE idвикладачі = %s"
        values = (surname, name, patronymic, birthdate, department_id, position, course, phone, teacher_id)
        cursor.execute(update_query, values)
        conn.commit()

        edit_window.destroy()

        refresh_treeview()

        messagebox.showinfo("Успіх!", "Дані викладача оновлені успішно.")

    selected_item = tree.selection()
    if selected_item:
        teacher_id = tree.item(selected_item)["text"]

        # Отримуємо дані викладача із бази даних
        cursor = conn.cursor()
        select_query = "SELECT прізвище, імя, по_батькові, дата_народження, idкафедри, посада, курс, телефон FROM викладачі WHERE idвикладачі = %s"
        cursor.execute(select_query, (teacher_id,))
        teacher_data = cursor.fetchone()

        if teacher_data:
            # Створюємо вікно для редагування
            edit_window = tk.Toplevel(root)
            edit_window.title("Редагувати викладача")


            name_label = tk.Label(edit_window, text="Прізвище:")
            name_label.grid(row=0, column=0, padx=5, pady=5)
            name_entry = tk.Entry(edit_window)
            name_entry.grid(row=0, column=1, padx=5, pady=5)
            name_entry.insert(0, teacher_data[0])

            surname_label = tk.Label(edit_window, text="Ім'я:")
            surname_label.grid(row=1, column=0, padx=5, pady=5)
            surname_entry = tk.Entry(edit_window)
            surname_entry.grid(row=1, column=1, padx=5, pady=5)
            surname_entry.insert(0, teacher_data[1])

            patronymic_label = tk.Label(edit_window, text="По-батькові:")
            patronymic_label.grid(row=2, column=0, padx=5, pady=5)
            patronymic_entry = tk.Entry(edit_window)
            patronymic_entry.grid(row=2, column=1, padx=5, pady=5)
            patronymic_entry.insert(0, teacher_data[2])

            birthdate_label = tk.Label(edit_window, text="Дата народження:")
            birthdate_label.grid(row=3, column=0, padx=5, pady=5)
            birthdate_entry = tk.Entry(edit_window)
            birthdate_entry.grid(row=3, column=1, padx=5, pady=5)
            birthdate_entry.insert(0, teacher_data[3])

            department_id_label = tk.Label(edit_window, text="ID кафедри:")
            department_id_label.grid(row=4, column=0, padx=5, pady=5)
            department_id_entry = tk.Entry(edit_window)
            department_id_entry.grid(row=4, column=1, padx=5, pady=5)
            department_id_entry.insert(0, teacher_data[4])

            position_label = tk.Label(edit_window, text="Посада:")
            position_label.grid(row=5, column=0, padx=5, pady=5)
            position_entry = tk.Entry(edit_window)
            position_entry.grid(row=5, column=1, padx=5, pady=5)
            position_entry.insert(0, teacher_data[5])

            course_label = tk.Label(edit_window, text="Курс:")
            course_label.grid(row=6, column=0, padx=5, pady=5)
            course_entry = tk.Entry(edit_window)
            course_entry.grid(row=6, column=1, padx=5, pady=5)
            course_entry.insert(0, teacher_data[6])

            phone_label = tk.Label(edit_window, text="Телефон:")
            phone_label.grid(row=7, column=0, padx=5, pady=5)
            phone_entry = tk.Entry(edit_window)
            phone_entry.grid(row=7, column=1, padx=5, pady=5)
            phone_entry.insert(0, teacher_data[7])

            save_button = tk.Button(edit_window, text="Зберегти", command=save_edited_teacher)
            save_button.grid(row=8, column=0, columnspan=2, padx=5, pady=5)
        else:
            messagebox.showerror("Помилка.", "Викладач не знайдений.")

def delete_teacher():
    selected_item = tree.selection()
    if selected_item:
        teacher_id = tree.item(selected_item)["text"]

        # Видаляємо викладача із бази даних
        cursor = conn.cursor()
        delete_query = "DELETE FROM викладачі WHERE idвикладачі = %s"
        cursor.execute(delete_query, (teacher_id,))
        conn.commit()

        tree.delete(selected_item)

        messagebox.showinfo("Успіх!", "Викладач видалений успішно.")


# Під'єднуємося до бази даних
conn = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="password",  # мій пароль
    database="db"
)

# Створюємо головне вікно
root = tk.Tk()
root.title("Викладачі кафедр факультету")

tree = ttk.Treeview(root)
tree["columns"] = ("прізвище", "імя", "по_батькові", "дата_народження", "idкафедри", "посада", "курс", "телефон")

tree.heading("#0", text="ID")
tree.heading("прізвище", text="Прізвище")
tree.heading("імя", text="Ім'я")
tree.heading("по_батькові", text="По-батькові")
tree.heading("дата_народження", text="Дата народження")
tree.heading("idкафедри", text="ID кафедри")
tree.heading("посада", text="Посада")
tree.heading("курс", text="Курс")
tree.heading("телефон", text="Телефон")

tree.column("#0", width=50)
tree.column("прізвище", width=100)
tree.column("імя", width=100)
tree.column("по_батькові", width=100)
tree.column("дата_народження", width=120)
tree.column("idкафедри", width=80)
tree.column("посада", width=80)
tree.column("курс", width=230)
tree.column("телефон", width=80)

# Отримуємо дані з бази даних і вставляємо їх у Treeview
refresh_treeview()

tree.pack()

def show_departments():
    department_window = tk.Toplevel(root)
    department_window.title("Кафедри")

    # Подключаємося до бази даних
    conn = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="password", # мій пароль
        database="db"
    )
    cursor = conn.cursor()

    department_tree = ttk.Treeview(department_window)
    department_tree["columns"] = ("назва_кафедри")

    department_tree.heading("#0", text="ID")
    department_tree.heading("назва_кафедри", text="Назва кафедри")

    department_tree.column("#0", width=50)
    department_tree.column("назва_кафедри", width=350)

    # Отримуємо дані з таблиці "кафедри"
    cursor.execute("SELECT idкафедри, назва_кафедри FROM кафедри")
    rows = cursor.fetchall()

    for row in rows:
        department_tree.insert("", "end", text=row[0], values=(row[1],))

    department_tree.pack()

    conn.close()

    def add_department():
        add_window = tk.Toplevel(root)
        add_window.title("Додати кафедру")
        add_window.geometry("270x80")

        label = tk.Label(add_window, text="Назва кафедри:")
        label.pack()

        entry = tk.Entry(add_window)
        entry.pack()

        button = tk.Button(add_window, text="Додати", command=lambda: insert_department(entry.get(), add_window))
        button.pack(pady=5)

    # Функція для вставки нової кафедри у базу даних
    def insert_department(department_name, add_window):
        conn = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="password",  # мій пароль
            database="db"
        )
        cursor = conn.cursor()

        # Вставляємо нову кафедру у таблицю "кафедри"
        insert_query = "INSERT INTO кафедри (назва_кафедри) VALUES (%s)"
        cursor.execute(insert_query, (department_name,))
        conn.commit()

        department_id = cursor.lastrowid

        department_tree.insert("", "end", text=department_id, values=(department_name,))

        conn.close()
        add_window.destroy()

    add_button = tk.Button(department_window, text="Додати кафедру", command=add_department)
    add_button.pack(side="left", padx=10, pady=5)


    def delete_department():
        selected_item = department_tree.selection()
        if selected_item:
            department_id = department_tree.item(selected_item)["text"]

            conn = mysql.connector.connect(
                host="127.0.0.1",
                user="root",
                password="password", # мій пароль
                database="db"
            )
            cursor = conn.cursor()

            # Видаляємо кафедру з бази даних
            delete_query = "DELETE FROM кафедри WHERE idкафедри = %s"
            cursor.execute(delete_query, (department_id,))
            conn.commit()

            department_tree.delete(selected_item)

            conn.close()

    delete_button = tk.Button(department_window, text="Видалити кафедру", command=delete_department)
    delete_button.pack(side="right", padx=10, pady=5)

# Створюємо кнопки для редагування, створення та видалення викладача, кнопку "Кафедри"
edit_button = tk.Button(root, text="Редагувати", command=edit_teacher)
add_button = tk.Button(root, text="Додати викладача", command=add_teacher)
delete_button = tk.Button(root, text="Видалити викладача", command=delete_teacher)
department_button = tk.Button(root, text="Кафедри", command=show_departments)

# Располагаем кнопки с помощью pack и настраиваем их расположение
delete_button.pack(side="right", padx=10, pady=5)
edit_button.pack(side="right", padx=10, pady=5)
add_button.pack(side="right", padx=10, pady=5)
department_button.pack(side="left", padx=10, pady=5)

# Запускаємо цикл подій Tkinter
root.mainloop()

# Закриваємо підключення до бази даних
conn.close()
