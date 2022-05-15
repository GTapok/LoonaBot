import sqlite3
conn = sqlite3.connect('users.db')
cur = conn.cursor()
def createDB():
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS users(name TEXT, id INT, arts INT)")
    conn.commit()
def UpVa(val_name, new_val, id):
    for row in cur.execute(f"SELECT {val_name} FROM users where id={id}"):
        new = row[0]+new_val
        cur.execute(f"UPDATE users SET {val_name}={new} where id={id}")
        conn.commit()

def InsrtValue(name, id):
    cur.execute(f'INSERT INTO users VALUES ("{name}", {id}, 0)')
    conn.commit()
