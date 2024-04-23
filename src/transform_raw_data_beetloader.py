import pandas as pd
import numpy as np
import argparse
import ast

def gps_coords(row, coord):
    try:
        return ast.literal_eval(row)[coord]
    except:
        return np.nan
    
def transform_csv(input_path, output_path):
    if output_path is None:
        output_path = '../data/processed/beetloader_processed.csv'
    cols_types = {'datapointid': 'str',
            'value': 'str', 
            'takenat': 'str', 
            'takenatend': 'str', 
            'postedat': 'str',
            'receivedat': 'str',
            'hour': 'float',
            'location': 'str',
            'algorithmversion': 'str',
            'processtype': 'str',
            'streamid': 'float',
            'additonaldata': 'str',
            'factory': 'float',
            'year': 'float',
            'month': 'float',
            'day' : 'float'}
    cols = list(cols_types.keys())

    df_raw = pd.read_csv(input_path, usecols=cols, dtype=cols_types)

    df_raw = pd.read_csv(input_path)
    df_raw['takenat'] = pd.to_datetime(df_raw['takenat'])
    df_raw = df_raw.sort_values(by=['takenat'])
    df_list = []

    for algo in df_raw['algorithmversion'].unique():
        # filter by algorithmversion
        df = df_raw[df_raw['algorithmversion'] == algo]
        # pivot values in datapointid column
        transformed = df.pivot_table(index='takenat', columns='datapointid', values='value', aggfunc='first').reset_index()
        
        # values from algorithmversion column
        algorithm_version = df.drop_duplicates(subset=['takenat', 'algorithmversion'])[['takenat', 'algorithmversion']]
        algorithm_version = algorithm_version.dropna()
        
        # values from factory column
        factory = df.drop_duplicates(subset=['takenat', 'factory'])[['takenat', 'factory']]
        factory = factory.dropna()
        # values from streamid column
        streamid = df.drop_duplicates(subset=['takenat', 'streamid'])[['takenat', 'streamid']]
        streamid = streamid.dropna()
        # values from processtype column
        # process_type = df.drop_duplicates(subset=['takenat', 'processtype'])[['takenat', 'processtype']]
        # process_type = process_type.dropna()
        
        transformed = transformed.merge(algorithm_version, on='takenat', how='left')
        transformed = transformed.merge(factory, on='takenat', how='left')
        transformed = transformed.merge(streamid, on='takenat', how='left')
        
        transformed['date'] = transformed['takenat'].dt.strftime('%m/%d/%Y')
        transformed['time'] = transformed['takenat'].dt.strftime('%I:%M:%S %p')
        transformed['hour'] = transformed['takenat'].dt.strftime('%H')
        transformed['minute'] = transformed['takenat'].dt.strftime('%M')
        transformed['seconds'] = transformed['takenat'].dt.strftime('%S')
        transformed['day'] = transformed['takenat'].dt.strftime('%d')
        transformed['month'] = transformed['takenat'].dt.strftime('%m')
        transformed['year'] = transformed['takenat'].dt.strftime('%Y')
        try:
            transformed = transformed.drop(columns=['beetloader_picture', 'beetloader_historical', ])
            transformed = transformed.dropna(subset=['beetloader_A', 'beetloader_B', 'beetloader_C', 'beetloader_beet_count', 'beetloader_empty_belt'], how='all')
        except:
            pass

        df_list.append(transformed)

    transformed_all = pd.concat(df_list)
    # values from location column
    locations = df_raw.drop_duplicates(subset=['takenat', 'location'])[['takenat', 'location']]
    locations = locations.dropna()
    transformed_all = transformed_all.merge(locations, on='takenat', how='left')
    transformed_all['latitude'] = transformed_all['location'].apply(lambda x: gps_coords(x, 0))
    transformed_all['longitude'] = transformed_all['location'].apply(lambda x: gps_coords(x, 1))
    transformed_all = transformed_all.drop(columns=['location'])
    transformed_all = transformed_all.sort_values(by=['takenat'])
    
    transformed_all = transformed_all[['takenat', 'beetloader_A', 'beetloader_B', 'beetloader_C',
       'beetloader_beet_count', 'beetloader_empty_belt', 'algorithmversion',
       'factory', 'streamid', 'latitude', 'longitude', 'date', 'time', 'hour',
       'minute', 'seconds', 'day', 'month', 'year']]
    
    # uncoment if you want to drop rows with NaN values in beetloader_A, beetloader_B, beetloader_C columns
    # transformed_all = transformed_all.dropna(subset=['beetloader_A', 'beetloader_B', 'beetloader_C'])
    # uncoment if you want to drop rows with beetloader_empty_belt == True
    # transformed_all = transformed_all[transformed_all['beetloader_empty_belt'] != 'True']
    transformed_all.to_csv(output_path, index=False)
        


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Transform raw beetloader data file.")
    parser.add_argument('--input', required=True, help='Path to the input CSV file.')
    parser.add_argument('--output', help='Path to save the transformed file.')
    args = parser.parse_args()
    
    transform_csv(args.input, args.output)
