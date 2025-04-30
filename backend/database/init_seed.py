from database.sql.sql_seed import seed_sql, is_sql_seeded
from database.mongodb.mongo_seed import seed_mongo, is_mongo_seeded

def seed_dummy_data():
    if not is_mongo_seeded():
        seed_mongo()
    else:
        print("MongoDB database already seeded. No need to add dummy data.")

    if not is_sql_seeded():
        seed_sql()
    else:
        print("MySQL database already seeded. No need to add dummy data.")
