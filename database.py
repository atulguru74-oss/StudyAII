import sqlite3

DB_NAME = "studyai.db"


def get_connection():
    return sqlite3.connect(DB_NAME, check_same_thread=False)


def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT,
        xp INTEGER DEFAULT 0,
        level TEXT DEFAULT 'Beginner'
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS quiz_results(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        subject TEXT,
        score INTEGER
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS study_plans(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        task TEXT,
        completed INTEGER DEFAULT 0
    )
    """)

    conn.commit()
    conn.close()


def add_user(username, password):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO users(username,password) VALUES(?,?)",
        (username, password)
    )

    conn.commit()
    conn.close()


def get_user(username):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE username=?",
        (username,)
    )

    user = cursor.fetchone()
    conn.close()

    return user


def update_xp(username, xp):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE users SET xp = xp + ? WHERE username=?",
        (xp, username)
    )

    conn.commit()
    conn.close()


def get_leaderboard():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT username,xp
    FROM users
    ORDER BY xp DESC
    LIMIT 10
    """)

    data = cursor.fetchall()

    conn.close()

    return data


def save_quiz_result(username, subject, score):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO quiz_results(username,subject,score)
        VALUES(?,?,?)
        """,
        (username, subject, score)
    )

    conn.commit()
    conn.close()


def get_user_results(username):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM quiz_results WHERE username=?",
        (username,)
    )

    data = cursor.fetchall()

    conn.close()

    return data

def get_user_xp(username):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT xp FROM users WHERE username=?",
        (username,)
    )

    xp = cursor.fetchone()

    conn.close()

    if xp:
        return xp[0]

    return 0

def get_user_info(username):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT username,xp
        FROM users
        WHERE username=?
        """,
        (username,)
    )

    data = cursor.fetchone()

    conn.close()

    return data


def calculate_level(xp):

    if xp < 100:
        return "Beginner"

    elif xp < 500:
        return "Learner"

    elif xp < 1000:
        return "Scholar"

    elif xp < 2500:
        return "Expert"

    else:
        return "Master"