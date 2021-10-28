import pymongo
import json
import pandas
from tabulate import tabulate
import logging
import exceptions
import time



def run_databse():

    start = time.time()
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    try:
        client.server_info()
    except :
        raise exceptions.connection_error('error to connect with database')

    # logging.debug("{}".format(client))
    print("client: ",client)
    print("connected to db: ",time.time()-start)

    db = client['songs_db']
    # print("server info : ",db.server_info())
    db_col = db['top_songs']
    filename = 'trending.json'
    with open(filename) as f:
        file_data = json.load(f)





    db_col.delete_many({})
    # total_songs_in_document = db_col.count_documents({})
    # print("total songs: ", total_songs_in_document)

    db_col.insert_many(file_data)

    # total_songs_in_document = db_col.count_documents({})
    # print("total songs: ", total_songs_in_document)

    alldbs = client.list_database_names()

    # print(alldbs)
    all_docs_in_songs_db = client['songs_db']
    # print(all_docs_in_songs_db)
    # print(all_docs_in_songs_db.list_collection_names())
    all_docs_in_songs_db_docs = all_docs_in_songs_db['top_songs']
    # print(all_docs_in_songs_db)
    data = db_col.find({}, {"_id": 0})
    all_song = []

    for item in data:
        song = {}
        song['Track'] = item['Track']
        song['Artists'] = item['Artists']
        song['Duration'] = item['Duration']
        all_song.append(song)

    df = pandas.DataFrame(all_song)
    df.index += 1
    print(tabulate(df,  headers=df.columns))