import psycopg2


conn = psycopg2.connect(
    database = 'felipeDB',
    user = 'felipe',
    password = '12234',
    host = 'localhost',
    port = '3383'
)
conn.cursor()

print(conn)
