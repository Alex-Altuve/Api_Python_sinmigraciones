import psycopg

class UserConection():
    conn = None
    
    def __init__(self):
        try:
            self.conn = psycopg.connect("dbname=Practica_Python user=postgres password=adminadmin host=localhost port=5432")
        except psycopg.OperationalError as err:
            print (err)
            self.conn.close()

    def write(self,data):
        with self.conn.cursor() as cur:
            cur.execute(""" INSERT INTO "usuarios"(name,phone) VALUES(%(name)s, %(phone)s)""",data)
        self.conn.commit()

    def read_all(self):
        with self.conn.cursor() as cur:
            data =cur.execute(""" SELECT * FROM "usuarios" """)
            return data.fetchall()

    def read_one(self, id):
        with self.conn.cursor() as cur:
            data = cur.execute(""" SELECT * FROM "usuarios" WHERE id= %s """,(id,))
        return data.fetchone() 
        ##eso es para hacer referencia que el %s es ese id si fuera otro se pondria, %i integer o %s string, despues en donde esta el corchete poner todos los parametros que se estan pasando 

    def delete(self, id):
        with self.conn.cursor() as cur: 
            cur.execute(""" DELETE FROM "usuarios" WHERE id = %s  """, (id, ))  
        self.conn.commit()

    def uptade(self, data):
        with self.conn.cursor() as cur: 
            cur.execute(""" UPDATE "usuarios" SET name = %(name)s, phone = %(phone)s WHERE id = %(id)s  """, data)  
        self.conn.commit()
    def __def__(self):
        self.conn.close()   