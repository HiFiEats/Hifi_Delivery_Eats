import sqlite3

conn = sqlite3.connect('existing_database.db')
cursor = conn.cursor()
cursor.execute('UPDATE Orders SET customer_id = ? WHERE customer_id = ?', (7, 1))
cursor.execute('UPDATE Orders SET customer_id = ? WHERE customer_id = ?', (8, 3))
cursor.execute('UPDATE Orders SET customer_id = ? WHERE customer_id = ?', (9, 4))
cursor.execute('UPDATE Orders SET customer_id = ? WHERE customer_id = ?', (10, 5))
cursor.execute('UPDATE Orders SET customer_id = ? WHERE customer_id = ?', (11, 6))
conn.commit()
conn.close()