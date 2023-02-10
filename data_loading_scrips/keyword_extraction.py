import pandas as pd
import yake


def concat_dialogs(df):
    """ Concatenate the dialogs in the dataframe """
    df_dialog_questions = df[df['to'].isna()]
    df_dialog_questions = df_dialog_questions.drop(['folder', 'date', 'from', 'to'], axis=1)
    df_dialog_questions = df_dialog_questions.fillna('').groupby(['dialogueID'])['text'].apply(' '.join).reset_index()
    df_dialog_answers = df[~df['to'].isna()]
    df_dialog_answers = df_dialog_answers.drop(['folder', 'date', 'from', 'to'], axis=1)
    df_dialog_answers = df_dialog_answers.fillna('').groupby(['dialogueID'])['text'].apply(' '.join).reset_index()
    df_dialog_text_concat = pd.concat([df_dialog_questions, df_dialog_answers], ignore_index=True)
    df_dialog_text_concat = df_dialog_text_concat.groupby(['dialogueID'])['text'].apply(' '.join).reset_index()
    df_dialog_text_concat['text'] = df_dialog_text_concat['text'].str.lower()
    return df_dialog_text_concat


def extract_keywords(df_dialog_text_concat, language, max_ngram_size, deduplication_thresold, deduplication_algo,
                     window_size, num_of_keywords):
    """ Extract keywords from the dialogs in the dataframe """

    keywords = []
    id_row = []
    custom_kw_extractor = yake.KeywordExtractor(lan=language, n=max_ngram_size, dedupLim=deduplication_thresold,
                                                dedupFunc=deduplication_algo, windowsSize=window_size,
                                                top=num_of_keywords, features=None)
    for index, row in df_dialog_text_concat.iterrows():
        keywords.append(custom_kw_extractor.extract_keywords(row['text']))
        id_row.append(row['dialogueID'])
    keywords_dict = {}
    for i in range(len(keywords)):
        row_list = []
        for j in range(len(keywords[i])):
            row_list.append(keywords[i][j][0])
        keywords_dict[id_row[i]] = row_list

    return keywords_dict


def extract_keywords_from_string(string, language, max_ngram_size, deduplication_thresold, deduplication_algo,
                                 window_size, num_of_keywords):
    """ Extract keywords from a string """
    string = string.lower()
    custom_kw_extractor = yake.KeywordExtractor(lan=language, n=max_ngram_size, dedupLim=deduplication_thresold,
                                                dedupFunc=deduplication_algo, windowsSize=window_size,
                                                top=num_of_keywords, features=None)
    keywords_raw = custom_kw_extractor.extract_keywords(string)
    keywords = []
    for i in range(len(keywords_raw[0])):
        keywords.append(keywords_raw[0][i])
    return keywords
