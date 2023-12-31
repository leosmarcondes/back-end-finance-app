from dotenv import dotenv_values

DATABASEUSER = dotenv_values('.env')
DATABASEINFO = f"mysql://{DATABASEUSER['USER']}:{DATABASEUSER['PASSWORD']}@{DATABASEUSER['HOST']}:{DATABASEUSER['PORT']}/{DATABASEUSER['DATABASE']}"
DATABASEFOLDER = "./database"