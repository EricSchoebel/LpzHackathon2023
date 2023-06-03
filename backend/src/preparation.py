import pandas as pd
import os

# Get the directory of the script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Constructing and normalizing the relative path to the JSON file
json_file_path_a = os.path.join(script_dir, '..', 'files', 'json_files', 'a.json')
json_file_path_b = os.path.join(script_dir, '..', 'files', 'json_files', 'b.json')
json_file_path_c = os.path.join(script_dir, '..', 'files', 'json_files', 'c.json')
json_file_path_d = os.path.join(script_dir, '..', 'files', 'json_files', 'd.json')
json_file_path_e = os.path.join(script_dir, '..', 'files', 'json_files', 'e.json')
json_file_path_f = os.path.join(script_dir, '..', 'files', 'json_files', 'f.json')
json_file_path_g = os.path.join(script_dir, '..', 'files', 'json_files', 'g.json')

# Load data from JSON files
data = pd.read_json(json_file_path_a, orient='records')
data2 = pd.read_json(json_file_path_b, orient='records')
data3 = pd.read_json(json_file_path_c, orient='records')
data4 = pd.read_json(json_file_path_d, orient='records')
data5 = pd.read_json(json_file_path_e, orient='records')
data6 = pd.read_json(json_file_path_f, orient='records')
data7 = pd.read_json(json_file_path_g, orient='records')
df = pd.concat([data, data2, data3, data4, data5, data6, data7])

print("--Bereite Datensatz vor ... --")

filtered0_data = df.sort_values('ortsteil')

filtered1_data = filtered0_data
#for testing: filtered1_data = filtered0_data[  (filtered0_data['ortsteil'].isin(['Holzhausen','Heiterblick']))   ]
                # Filter the data based on a condition
                #filtered1_data = data[  (data['ortsteil'] == 'Holzhausen')   ]

filtered2_data = filtered1_data[ filtered1_data['ortsteil'].notnull()   # we do not want "Stadtbezirk"-aggregation
    & filtered1_data['jahr'].between(2021, 2021)    #only 2021 has (almost) all values for the categories
                              #for testing:  & filtered1_data['ortsteil']=='Heiterblick'
    & ( filtered1_data['name'].isin(['Durchschnittsalter', 'Jugendquote', 'Altenquote', 'Kinder insgesamt',
                                     'Durchschnittliche Haushaltsgröße',
                                     'Zukunftsaussicht', 'Wirtschaftliche Lage','Lebenszufriedenheit','Wohnviertel', # 4 Zufriedenheitsfaktoren
                                     'Persönliches Einkommen','   mit Elektromotor', 'Straftaten insgesamt' ]) )
        ]

# create dictionary of unique values and their corresponding IDs
ortsteil_dict = { ortsteil : i  # key : value
                  for i, ortsteil in enumerate(filtered2_data['ortsteil'].unique()) }

filtered3_data = filtered2_data.copy(deep=True)
# create new 'ortsteil_id' column using the dictionary to map values to IDs
filtered3_data['ortsteil_id'] = filtered2_data['ortsteil'].map(ortsteil_dict) #function "map" takes keys as input and gives values as output

filtered4_data = filtered3_data[['ortsteil_id','ortsteil', 'name', 'wert', 'jahr']] #IMPORTANT: DO NOT FORGET TO DO DOUBLE SQUARE BRACKETS

# pivot the dataframe (in order to get information from "name"-column in several columns)
#take as new columns th stuff from column 'name', as new cell values take content of 'wert, do this for every diferent "ortsteil_id, ortsteil" combination
df_pivot = filtered4_data.pivot(index=['ortsteil_id','ortsteil'], columns='name', values='wert') #USEFUL PIVOT-function

# reset the index
df_pivot = df_pivot.reset_index()

#Renaming columns, left old, right new
df_pivot = df_pivot.rename(columns={ 'Kinder insgesamt': 'KitaKinder',
                                     'Straftaten insgesamt': 'Straftaten',
                                     '   mit Elektromotor': 'Elektroautos',
                                     'Lebenszufriedenheit': 'LebenszufriedenheitZufriedenheitsfaktor',
                                     'Wohnviertel':'WohnviertelZufriedenheitsfaktor',
                                     'Zukunftsaussicht':'ZukunftsaussichtZufriedenheitsfaktor',
                                     'Wirtschaftliche Lage': 'WirtschaftlicheLageZufriedenheitsfaktor',
                                     'ortsteil': 'Ortsteil',
                                     'ortsteil_id': 'Ortsteil_ID',
                                     'Durchschnittliche Haushaltsgröße':'DurchschnittlicheHaushaltsgröße',
                                     'Persönliches Einkommen':'PersönlichesEinkommen'
                                     })

columns = df_pivot.columns.tolist()
columns[2], columns[3] = columns[3], columns[2]
df_pivot = df_pivot[columns]

print('----------------')

for col in df_pivot.columns:
    try:
        #convert to string, then slice, then to float (before: values too long for float)
        if col != 'Ortsteil': # Ortsteile should not be shortened
            df_pivot[col] = df_pivot[col].astype(str)
            df_pivot[col] = df_pivot[col].str.slice(stop=7)
            df_pivot[col] = df_pivot[col].str.replace(',', '.').astype(float)
    except ValueError:
        pass

column_names = df_pivot.columns.tolist()
new_column_order = [
    column_names[0],
    column_names[1],
    column_names[2],
    column_names[4],
    column_names[5],
    column_names[3],
    column_names[6],
    column_names[7],
    column_names[8],
    column_names[9],
    column_names[10],
    column_names[11],
    column_names[12],
    column_names[13]
]
df_pivot = df_pivot[new_column_order]

print("--Datensatz vorbereitet--")






