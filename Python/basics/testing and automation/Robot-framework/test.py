import pyodbc

connection_string = "DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost\\SQLEXPRESS;DATABASE=DEVELOP;UID=oskari;PWD=admin123"

try:
    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()
    cursor.execute("SELECT TOP 5 * FROM PPM.T_USER")
    for row in cursor:
        print(row)
    conn.close()
except Exception as e:
    print(f"Error: {e}")