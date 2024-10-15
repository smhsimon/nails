import os
import pandas as pd
import datetime

def csv_to_json(csv_path, biweekly_bool):
    if biweekly_bool:
        df = pd.read_csv(csv_path, index_col=0)
    if not biweekly_bool:
        df = pd.read_csv(csv_path, index_col=False)
    
    base = os.path.splitext(os.path.basename(csv_path))[0]
    path = os.path.join(os.path.dirname(csv_path), base + '.json')

    df.to_json(path)

# def json_to_csv(json_path, biweekly_bool):
#     df = pd.read_json(json_path)
#     if biweekly_bool:
#         df.reset_index(inplace=True)
#         df['index'] = pd.to_datetime(df['index'])
#         df['index'] = df['index'].dt.strftime('%B %d, %Y')
#         df.rename(columns={'index': 'date'}, inplace=True)
#         df.to_csv('cat.csv', index=False)
    
#     if not biweekly_bool:
#         df.to_csv('cat.csv', index=0)


path = os.path.join('employee data', 'Amy', 'Amy_biweekly.csv')
path2 = os.path.join('employee data', 'Amy', 'Amy_today.csv')

path3 = os.path.join('employee data', 'Amy', 'Amy_biweekly.json')
path4 = os.path.join('employee data', 'Amy', 'Amy_today.json')

# csv_to_json(path, True)
csv_to_json(path2, False)
# json_to_csv(path3)
json_to_csv(path4, False)