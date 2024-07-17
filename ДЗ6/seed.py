import psycopg2
from faker import Faker

def seed_data():
    try:
        
        conn = psycopg2.connect(
            dbname="task_management",
            user="postgres", 
            password="1001",  
            host="localhost"
        )
        cursor = conn.cursor()

        fake = Faker()

        for _ in range(10):
            fullname = fake.name()
            email = fake.unique.email()
            cursor.execute("INSERT INTO users (fullname, email) VALUES (%s, %s)", (fullname, email))

       
        for _ in range(20):
            title = fake.sentence(nb_words=6)
            description = fake.text()
            status_id = fake.random_int(min=1, max=3)
            user_id = fake.random_int(min=1, max=10)
            cursor.execute("INSERT INTO tasks (title, description, status_id, user_id) VALUES (%s, %s, %s, %s)", 
                           (title, description, status_id, user_id))

        
        conn.commit()

        
        cursor.close()
        conn.close()

    except Exception as error:
        print(f"Помилка при заповненні таблиць даними: {error}")

if __name__ == '__main__':
    seed_data()
