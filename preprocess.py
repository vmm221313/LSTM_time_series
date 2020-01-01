import pandas as po
import os
from tqdm import tqdm_notebook
import os


def get_data_for_given_ticker(ticker):
    try:
        df = po.read_csv('merged_data/' + ticker + 'merged.csv')
        df = df[:int(0.005*len(df))]
        train = df.drop(['time', 'date', '#RIC', 'class', 'Expected Return'], axis = 1)
        targets = df['class']
        
        train = train[train.columns[:22]]
        #print(train.columns)
        #df = df.sort_values(['date', 'time']).reset_index(drop=True)
        #df.to_csv('merged_data/' + ticker + 'merged.csv', index = False)
    except FileNotFoundError:
        print('Concatenated DataFrame not found, creating from source files')
        df = po.DataFrame()
        for _, _, ticker_files in os.walk('data/'+ticker+'/'):
            for file in tqdm_notebook(sorted(ticker_files)):
                df_t = po.read_csv('data/'+ticker+'/'+file)
                df = df.append(df_t).reset_index(drop = True)
            del df_t
        df = df.drop(['volat', 'temp', 'ass', 'count'], axis = 1)
        df = df.sort_values(['date', 'time']).reset_index(drop_index=True)
        df.to_csv('concatenated_data/' + ticker + '.csv', index = False)
        train = df.drop(['time', 'date', '#RIC', 'class'], axis = 1)
        targets = df['class']
    return train, targets


ticker_embeddings_df = po.read_csv('more_data/ticker_embeddings.csv')

tickers = ticker_embeddings_df['#RIC'].unique()
del ticker_embeddings_df

tickers

df = po.read_csv('merged_data/' + 'CLc1' + 'merged.csv')

target = df['class']

df = df[df.columns[:26]]

df['class'] = target

df





for ticker in tickers:
    

for ticker


def create_merged_data_without_embeddings():
    for ticker in tqdm_notebook(tickers):
        df = po.read_csv('merged_data/' + ticker + 'merged.csv')   
        target = df['class']
        df = df[df.columns[:26]]
        df['class'] = target
        df = df.sort_values(['date', 'time']).reset_index(drop=True)
        df.to_csv('merged_data_without_embeddings/' + ticker + 'merged.csv', index = False)


create_merged_data_without_embeddings()


