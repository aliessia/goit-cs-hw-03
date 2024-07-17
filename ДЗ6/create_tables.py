import psycopg2

def create_tables():
    commands = (
        """
        CREATE TABLE users (
            id SERIAL PRIMARY KEY,
            fullname VARCHAR(100) NOT NULL,
            email VARCHAR(100) UNIQUE NOT NULL
        )
        """,
        """
        CREATE TABLE status (
            id SERIAL PRIMARY KEY,
            name VARCHAR(50) UNIQUE NOT NULL
        )
        """,
        """
        INSERT INTO status (name) VALUES 
        ('new'),
        ('in progress'),
        ('completed')
        """,
        """
        CREATE TABLE tasks (
            id SERIAL PRIMARY KEY,
            title VARCHAR(100) NOT NULL,
            description TEXT,
            status_id INTEGER NOT NULL,
            user_id INTEGER NOT NULL,
            FOREIGN KEY (status_id) REFERENCES status(id),
            FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
        )
        """
    )

    try:
   
        conn = psycopg2.connect(
            dbname="task_management",
            user="postgres", 
            password="1001", 
            host="localhost"
        )
        cursor = conn.cursor()
        
        
        for command in commands:
            cursor.execute(command)
        
      
        conn.commit()

       
        cursor.close()
        conn.close()

    except Exception as error:
        print(f"Помилка при створенні таблиць: {error}")

if __name__ == '__main__':
    create_tables()
