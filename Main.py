import data_loading_scrips.data_loading_script as dls
import data_loading_scrips.keyword_extraction as ke

if __name__ == '__main__':
    """df = dls.load_data_from_csv('Data', 'xxxx.csv')  # load data from csv, sobstitute 'xxxx' with the name of the 
    # csv file

    password = "xxxx"  # sobstitute 'xxxx' with the password of the mongo database
    mongodb_url_string = "xxxx:" + password + "xxxx"  # sobstitute 'xxxx' with the url of the mongo
    # cluster

    dls.load_df_to_mongo(df, mongodb_url_string, 'xxxx')  # load data to mongo, sobstitute 'xxxx' with the name of the
    # database
    """

    df = dls.load_data_from_csv('Data', 'dialogueTextFirst505.csv')
    df_keywords = ke.concat_dialogs(df)
    keywords_dict = ke.extract_keywords(df_keywords, 'en', 2, 0.9, 'seqm', 1, 4)
    password = "8ST3ESqAjlUEbLUB"
    mongodb_url_string = "mongodb+srv://DB_Admin:" + password + "@cluster0.svikscz.mongodb.net"
    dls.load_df_to_mongo(df, mongodb_url_string, 'Test505')
    dls.load_keywords_to_mongo(keywords_dict, mongodb_url_string, 'Test505')

