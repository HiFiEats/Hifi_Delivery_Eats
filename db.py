import sqlite3

conn = sqlite3.connect('existing_database.db')
cursor = conn.cursor()
cursor.execute('UPDATE Users SET is_active = ? WHERE user_id = ?', (1, 11))
cursor.execute('UPDATE Users SET is_active = ? WHERE user_id = ?', (1, 7))
cursor.execute('UPDATE Users SET is_active = ? WHERE user_id = ?', (1, 9))
cursor.execute('UPDATE Users SET is_active = ? WHERE user_id = ?', (1, 10))
conn.commit()
conn.close()