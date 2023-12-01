from pydal import DAL, Field
from config import DATABASEUSER, DATABASEINFO, DATABASEFOLDER
import os

def model():

    dbinfo = DATABASEINFO
    folder = DATABASEFOLDER
    
    os.makedirs(folder, exist_ok=True)

    database = DAL(dbinfo, db_codec='UTF-8', folder=folder, pool_size=1)

    table(database)

    return database

def table(database):
    database.define_table("transations",
                          Field("amount", "double"),
                          Field("category", "string"),
                          Field("description", "string"),
                          Field("is_income", "boolean"),
                          Field("date", "string")
    )

if __name__ == "__main__":
    model()