import pandas as pd
import pymongo
import dns
from pymongo import MongoClient
import json


def load_data_from_csv(path, filename):
    """ Load data from csv file and return a pandas dataframe """
    df = pd.read_csv(path + '/' + filename)  # read csv file
    return df


def load_df_to_mongo(df, mongo_uri, mongo_db):
    """ Load a pandas dataframe to a mongo database """
    client = MongoClient(mongo_uri)
    db = client[mongo_db]
    for index, row in df.iterrows():  # iterate over rows in dataframe
        row_id = row['dialogueID']

        # check if dialogeID already exists and if so it means it's the same conversation just upadates the document
        if db.dialogs.count_documents({"dialogueID": row_id}, limit=1) != 0:

            domanda = row['to']
            if pd.isnull(domanda):  # check if the row is a question
                type_sent = 'Domanda'
            else:
                type_sent = 'Risposta'
            db.dialogs.update_one({'dialogueID': row_id}, {'$addToSet': {'chat': [{"sentence": row['text'],
                                                                                   "type": type_sent}]}})
        else:
            domanda = row['to']
            if pd.isnull(domanda):
                testo = {
                    "dialogueID": row_id,
                    "chat": [{
                        "sentence": row['text'],
                        "type": "Domanda"
                    }]
                }
            else:
                testo = {
                    "dialogueID": row_id,
                    "chat": [{
                        "sentence": row['text'],
                        "type": "Risposta"
                    }]
                }
            db.dialogs.insert_one(testo)  # insert the document in the collection
