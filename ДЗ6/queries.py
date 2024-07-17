import psycopg2

def get_connection():
    return psycopg2.connect(
        dbname="task_management",
        user="postgres",
        password="1001",
        host="localhost"
    )

# 1. Отримати всі завдання певного користувача
def get_tasks_by_user(user_id):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        query = "SELECT * FROM tasks WHERE user_id = %s;"
        cursor.execute(query, (user_id,))
        tasks = cursor.fetchall()
        for task in tasks:
            print(task)
        cursor.close()
        conn.close()
    except Exception as error:
        print(f"Помилка при отриманні завдань: {error}")

# 2. Вибрати завдання за певним статусом
def get_tasks_by_status(status_name):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        query = """
        SELECT * FROM tasks WHERE status_id = (SELECT id FROM status WHERE name = %s);
        """
        cursor.execute(query, (status_name,))
        tasks = cursor.fetchall()
        for task in tasks:
            print(task)
        cursor.close()
        conn.close()
    except Exception as error:
        print(f"Помилка при отриманні завдань: {error}")

# 3. Оновити статус конкретного завдання
def update_task_status(task_id, new_status):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        query = """
        UPDATE tasks 
        SET status_id = (SELECT id FROM status WHERE name = %s)
        WHERE id = %s;
        """
        cursor.execute(query, (new_status, task_id))
        conn.commit()
        cursor.close()
        conn.close()
        print("Статус завдання оновлено")
    except Exception as error:
        print(f"Помилка при оновленні статусу завдання: {error}")

# 4. Отримати список користувачів, які не мають жодного завдання
def get_users_without_tasks():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        query = """
        SELECT * FROM users WHERE id NOT IN (SELECT DISTINCT user_id FROM tasks);
        """
        cursor.execute(query)
        users = cursor.fetchall()
        for user in users:
            print(user)
        cursor.close()
        conn.close()
    except Exception as error:
        print(f"Помилка при отриманні користувачів: {error}")

# 5. Додати нове завдання для конкретного користувача
def add_new_task(title, description, status_name, user_id):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        query = """
        INSERT INTO tasks (title, description, status_id, user_id)
        VALUES (%s, %s, (SELECT id FROM status WHERE name = %s), %s);
        """
        cursor.execute(query, (title, description, status_name, user_id))
        conn.commit()
        cursor.close()
        conn.close()
        print("Нове завдання додано")
    except Exception as error:
        print(f"Помилка при додаванні завдання: {error}")

# 6. Отримати всі завдання, які ще не завершено
def get_uncompleted_tasks():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        query = """
        SELECT * FROM tasks WHERE status_id != (SELECT id FROM status WHERE name = 'completed');
        """
        cursor.execute(query)
        tasks = cursor.fetchall()
        for task in tasks:
            print(task)
        cursor.close()
        conn.close()
    except Exception as error:
        print(f"Помилка при отриманні завдань: {error}")

# 7. Видалити конкретне завдання
def delete_task(task_id):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        query = "DELETE FROM tasks WHERE id = %s;"
        cursor.execute(query, (task_id,))
        conn.commit()
        cursor.close()
        conn.close()
        print("Завдання видалено")
    except Exception as error:
        print(f"Помилка при видаленні завдання: {error}")

# 8. Знайти користувачів з певною електронною поштою
def find_users_by_email(email_pattern):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        query = "SELECT * FROM users WHERE email LIKE %s;"
        cursor.execute(query, (email_pattern,))
        users = cursor.fetchall()
        for user in users:
            print(user)
        cursor.close()
        conn.close()
    except Exception as error:
        print(f"Помилка при пошуку користувачів: {error}")

# 9. Оновити ім'я користувача
def update_user_name(user_id, new_name):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        query = "UPDATE users SET fullname = %s WHERE id = %s;"
        cursor.execute(query, (new_name, user_id))
        conn.commit()
        cursor.close()
        conn.close()
        print("Ім'я користувача оновлено")
    except Exception as error:
        print(f"Помилка при оновленні імені користувача: {error}")

# 10. Отримати кількість завдань для кожного статусу
def get_task_count_by_status():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        query = """
        SELECT s.name, COUNT(t.id) 
        FROM tasks t
        JOIN status s ON t.status_id = s.id
        GROUP BY s.name;
        """
        cursor.execute(query)
        results = cursor.fetchall()
        for result in results:
            print(result)
        cursor.close()
        conn.close()
    except Exception as error:
        print(f"Помилка при отриманні кількості завдань: {error}")

# 11. Отримати завдання, які призначені користувачам з певною доменною частиною електронної пошти
def get_tasks_by_user_email_domain(domain):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        query = """
        SELECT t.* 
        FROM tasks t
        JOIN users u ON t.user_id = u.id
        WHERE u.email LIKE %s;
        """
        cursor.execute(query, (domain,))
        tasks = cursor.fetchall()
        for task in tasks:
            print(task)
        cursor.close()
        conn.close()
    except Exception as error:
        print(f"Помилка при отриманні завдань: {error}")

# 12. Отримати список завдань, що не мають опису
def get_tasks_without_description():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        query = "SELECT * FROM tasks WHERE description IS NULL OR description = '';"
        cursor.execute(query)
        tasks = cursor.fetchall()
        for task in tasks:
            print(task)
        cursor.close()
        conn.close()
    except Exception as error:
        print(f"Помилка при отриманні завдань: {error}")

# 13. Вибрати користувачів та їхні завдання, які є у статусі 'in progress'
def get_users_and_tasks_in_progress():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        query = """
        SELECT u.*, t.* 
        FROM users u
        JOIN tasks t ON u.id = t.user_id
        JOIN status s ON t.status_id = s.id
        WHERE s.name = 'in progress';
        """
        cursor.execute(query)
        results = cursor.fetchall()
        for result in results:
            print(result)
        cursor.close()
        conn.close()
    except Exception as error:
        print(f"Помилка при отриманні завдань: {error}")

# 14. Отримати користувачів та кількість їхніх завдань
def get_users_and_task_counts():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        query = """
        SELECT u.id, u.fullname, COUNT(t.id) 
        FROM users u
        LEFT JOIN tasks t ON u.id = t.user_id
        GROUP BY u.id, u.fullname;
        """
        cursor.execute(query)
        results = cursor.fetchall()
        for result in results:
            print(result)
        cursor.close()
        conn.close()
    except Exception as error:
        print(f"Помилка при отриманні кількості завдань: {error}")

# Приклад виклику функцій:
# get_tasks_by_user(1)
# get_tasks_by_status('new')
# update_task_status(1, 'in progress')
# get_users_without_tasks()
# add_new_task('New Task', 'Task Description', 'new', 1)
# get_uncompleted_tasks()
# delete_task(1)
# find_users_by_email('%@example.com')
# update_user_name(1, 'New Name')
# get_task_count_by_status()
# get_tasks_by_user_email_domain('%@example.com')
# get_tasks_without_description()
# get_users_and_tasks_in_progress()
# get_users_and_task_counts()
