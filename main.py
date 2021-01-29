from admin_database import database as database

#------------------Test Methods----------------------------
con=database.sql_connection()
database.sql_table(con)
entities = (2, 'Andrew', 800, 'IT', 'Tech', '2018-02-06')
database.add_user(con,entities)
database.search_user(con,2)
database.delete_user(con,2)
print("A")