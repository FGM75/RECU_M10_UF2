import psycopg2


conn = psycopg2.connect(
    database = 'felipeDB',
    host='localhost',
    user="felipe",
    password="1234",
    port = '3383'
)


cur = conn.cursor()


sql= """
CREATE TABLE persona(
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    apellido VARCHAR(255) NOT NULL,
    colorFavorito VARCHAR(255) NOT NULL,
    edad BIGINT NOT NULL
)
"""


cur.execute(sql)

conn.commit()

conn.close()
