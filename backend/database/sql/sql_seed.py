import pymysql
import os 
import glob

sql_conn = pymysql.connect(
    host="sql",
    user="root",
    password="password",
    database="hypertrophy_edu_sqldb"
)

def is_sql_seeded():
    with sql_conn.cursor() as cursor:
        cursor.execute("SELECT COUNT(*) FROM user")  # adjust table
        count = cursor.fetchone()[0]
        return count > 0

def seed_sql():
    print("Seeding MySQL from SQL file...")

    dummy_data_file = glob.glob(os.path.join(os.path.dirname(__file__), "sqldummydata", "sqldummydata.sql"))

    with open(dummy_data_file[0], "r") as file:
        sql_script = file.read()

    with sql_conn.cursor() as cursor:
        for statement in sql_script.strip().split(";"):
            if statement.strip():
                cursor.execute(statement + ";")
    
    print("sqldummydata.sql successfully seeded into database.")
