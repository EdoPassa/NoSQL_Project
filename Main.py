import data_loading_scrips.data_loading_script as dls

if __name__ == '__main__':
    df = dls.load_data_from_csv('Data', 'dialogueTextFirst505.csv')
    password = "8ST3ESqAjlUEbLUB"
    mongodb_url_string = "mongodb+srv://DB_Admin:" + password + "@cluster0.svikscz.mongodb.net/test"
    dls.load_df_to_mongo(df, mongodb_url_string, 'customer_support')
