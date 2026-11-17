
from connect import connect

conn = connect()

if conn:
    conn.close()
    print("Connection test completed!")
