import sqlite3


class SingletonMeta(type):
    _instance={}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            instance=super().__call__(*args,**kwargs)
            cls._instance[cls]=instance
        return cls._instance[cls]
#database connection singleton
class DatabaseConnection(metaclass=SingletonMeta):
    def __init__(self,db_name="main_server.db"):
        self.connection=sqlite3.connect(db_name)
        print("database connection initialZed")
    def execute(self,query,params=None):
        cursor=self.connection.cursor()
        cursor.execute(query,params or [])
        self.connection.commit()
        return cursor.fetchall()
    def close(self):
        self.connection.close()
#Example usage
db1=DatabaseConnection()
db2=DatabaseConnection()

print(f"Same DB instance? {db1 is db2}")

# Create table and insert data
db1.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)")
db2.execute("INSERT INTO users (name) VALUES (?)", ("Syed",))

# Query data
rows = db2.execute("SELECT * FROM users")
print("Users in DB:", rows)

db1.close()