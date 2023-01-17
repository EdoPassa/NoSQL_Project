import pandas as pd
import pymongo
import dns
from pymongo import MongoClient
import json


def load_data_from_csv(path, filename):
    df = pd.read_csv(path + filename)
    return df


def load_df_to_mongo(df, mongo_uri, mongo_db):
    client = MongoClient(mongo_uri)
    db = client[mongo_db]
    for index, row in df.iterrows():
        id = row['dialogueID']
        if db.dialogs.count_documents({"dialogueID": id}, limit=1) != 0:
            domanda = row['to']
            if pd.isnull(domanda):
                type_sent = 'Domanda'
            else:
                type_sent = 'Risposta'
            db.dialogs.update_one({'dialogueID': id}, {'$addToSet': {'chat': [{"sentence": row['text'],
                                                                               "type": type_sent}]}})
        else:
            domanda = row['to']
            if pd.isnull(domanda):
                testo = {
                    "dialogueID": id,
                    "chat": [{
                        "sentence": row['text'],
                        "type": "Domanda"
                    }]
                }
            else:
                testo = {
                    "dialogueID": id,
                    "chat": [{
                        "sentence": row['text'],
                        "type": "Risposta"
                    }]
                }
            print(testo)
            db.dialogs.insert_one(testo)

