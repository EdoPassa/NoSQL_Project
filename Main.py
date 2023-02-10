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
    return


def query_new_question(user_question, mongo_uri, database):
    """ Query the mongo database and print the results"""
    print('\n')
    kw_question = ke.extract_keywords_from_string(user_question, 'en', 2, 0.9, 'seqm', 1, 4)
    conversations = dls.query_mongo(mongo_uri,
                                    database, kw_question) # query the mongo database
    doc_list = []
    # print the results
    for doc in conversations:
        doc_list.append(doc)
    for doc in doc_list:
        sentence_list = []
        for sentence in doc['chat']:
            sentence_list.append(sentence)
        for i in range(len(sentence_list)):
            if i == 0:
                print(sentence_list[i]['sentence'])
            else:
                print(sentence_list[i][0]['sentence'])
        print('\n')


if __name__ == '__main__':
    query_new_question(input("What's your question?: "),'xxx','xxx') # replace xxx with your mongo url and database name

