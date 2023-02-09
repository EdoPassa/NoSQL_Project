import data_loading_scrips.data_loading_script as dls
import data_loading_scrips.keyword_extraction as ke

def load_data(path, filename, mongodb_url_string, database_name):
    df = dls.load_data_from_csv(path, filename)  # load data from csv file
    dls.load_df_to_mongo(df, mongodb_url_string, database_name)  # load data to mongo database

def load_keywords(path, filename, mongodb_url_string, database_name):
    df = dls.load_data_from_csv(path, filename)
    df_keywords = ke.concat_dialogs(df)
    keywords_dict = ke.extract_keywords(df_keywords, 'en', 2, 0.9, 'seqm', 1, 4)
    dls.load_keywords_to_mongo(keywords_dict, mongodb_url_string, database_name)  # load keywords to mongo database

if __name__ == '__main__':

    # load_keywords('Data', 'dialogueTextFirst505.csv', 'mongodb+srv://DB_Admin:8ST3ESqAjlUEbLUB@cluster0.svikscz.mongodb.net', 'Test505')
    user_question = input("Inserisci la domanda: ")
    kw_question = ke.extract_keywords_from_string(user_question, 'en', 2, 0.9, 'seqm', 1, 4)
    print(dls.query_mongo('mongodb+srv://DB_Admin:8ST3ESqAjlUEbLUB@cluster0.svikscz.mongodb.net', 'Test505', kw_question))

