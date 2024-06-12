import psycopg2


conn = psycopg2.connect(
    database = 'felipeDB',
    host='localhost',
    user="felipe",
    password="1234",
    port = '3383'
)


cur = conn.cursor()


sql_insert= """
INSERT INTO persona(
'felipe','gonzalez','VerdeAprobado', 30
)
"""


cur.execute(sql_insert)

conn.commit()

conn.close()
