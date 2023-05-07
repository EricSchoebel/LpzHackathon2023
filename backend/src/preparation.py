"""

jsondata = '{"0001":{"FirstName":"John","LastName":"Mark","MiddleName":"Lewis","username":"johnlewis2","password":"2910"}' \
           '}'
jdata = json.loads(jsondata)
df = pd.DataFrame(jdata)
print(df.T)



dftrain = pd.read_csv('https://statistik.leipzig.de/opendata/api/values?kategorie_nr=14&rubrik_nr=8&periode=y&format=csv') # training data

dftrain2 = pd.read_csv('https://statistik.leipzig.de/opendata/api/kdvalues?kategorie_nr=2&rubrik_nr=2&periode=y&format=csv')


print(dftrain2)





Csv dateien runterladen und einlesen falls sich der link zu den mal ändert geht es sonst nicht.
Man kann ja die fkt trotzdem noch dazu machen dass man es auch direkt online einlesen würde

def kmeansMitK(liste von listeDerDimensionsKoordinaten, k):
   - halt Kmeans machen
   - return labelliste

def kmeansOhneK(liste von listeDerDimensionsKoordinaten):
     - determineOptimalK(liste von                                             listeDerDimensionsKoordinaten) returnt k
    - kmeansMitK(liste von listeDerDimensionsKoordinaten, k)




# Convert DataFrame to matrix
mat = dataset.values
# Using sklearn
km = sklearn.cluster.KMeans(n_clusters=5)
km.fit(mat)
# Get cluster assignment labels
labels = km.labels_
# Format results as a DataFrame
results = pandas.DataFrame([dataset.index,labels]).T




"""
import numpy as np
import pandas as pd
import json
import glob
import os



"""
data = []
file_list = glob.glob('files/json_files/*.json')

for file in file_list:
    with open(file, 'r') as f:
        json_data = json.load(f)
        data.append(json_data)

df = pd.DataFrame(data)

print(df.T)
"""

# Get the directory of the script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Constructing and normalizing the relative path to the JSON file
json_file_path_a = os.path.normpath(os.path.join(script_dir, '..', 'files', 'json_files', 'a.json'))
json_file_path_b = os.path.normpath(os.path.join(script_dir, '..', 'files', 'json_files', 'b.json'))
json_file_path_c = os.path.normpath(os.path.join(script_dir, '..', 'files', 'json_files', 'c.json'))
json_file_path_d = os.path.normpath(os.path.join(script_dir, '..', 'files', 'json_files', 'd.json'))
json_file_path_e = os.path.normpath(os.path.join(script_dir, '..', 'files', 'json_files', 'e.json'))
json_file_path_f = os.path.normpath(os.path.join(script_dir, '..', 'files', 'json_files', 'f.json'))
json_file_path_g = os.path.normpath(os.path.join(script_dir, '..', 'files', 'json_files', 'g.json'))

# Load data from JSON files
data = pd.read_json(json_file_path_a, orient='records')
data2 = pd.read_json(json_file_path_b, orient='records')
data3 = pd.read_json(json_file_path_c, orient='records')
data4 = pd.read_json(json_file_path_d, orient='records')
data5 = pd.read_json(json_file_path_e, orient='records')
data6 = pd.read_json(json_file_path_f, orient='records')
data7 = pd.read_json(json_file_path_g, orient='records')
df = pd.concat([data, data2, data3, data4, data5, data6, data7])

#print(data.head(5105))
#print(data.to_string())
# Filter the data based on a condition
#filtered1_data = data[  (data['ortsteil'] == 'Holzhausen')   ]
filtered0_data = df.sort_values('ortsteil')

filtered1_data = filtered0_data
#for testing: filtered1_data = filtered0_data[  (filtered0_data['ortsteil'].isin(['Holzhausen','Heiterblick']))   ]


filtered2_data = filtered1_data[ filtered1_data['ortsteil'].notnull()   # we do not want "Stadtbezirk"-aggregation
    & filtered1_data['jahr'].between(2021, 2021)    #only 2021 has all values for the categories
                              #for testing:  & filtered1_data['ortsteil']=='Heiterblick'
    & ( filtered1_data['name'].isin(['Durchschnittsalter', 'Jugendquote', 'Altenquote', 'Kinder insgesamt',
                                     'Durchschnittliche Haushaltsgröße',
                                     'Zukunftsaussicht', 'Wirtschaftliche Lage','Lebenszufriedenheit','Wohnviertel', # 4 Zufriedenheitsfaktoren
                                     'Persönliches Einkommen','   mit Elektromotor', 'Straftaten insgesamt' ]) )
                                ]


#pd.set_option('display.max_rows', None)
#pd.set_option('display.max_columns', None)
#print(filtered0_data[filtered0_data['ortsteil']=='Heiterblick'])
#vals = filtered1_data['name'].to_list()
#for val in vals:
#    print("A"+val+"B")
#print(vals)



# filtered2_data['wert'] = filtered2_data['wert'].round(3)

# create dictionary of unique values and their corresponding IDs
ortsteil_dict = { ortsteil : i  # key : value
                  for i, ortsteil in enumerate(filtered2_data['ortsteil'].unique()) }

#print(ortsteil_dict)

filtered3_data = filtered2_data.copy(deep=True)
# create new 'ortsteil_id' column using the dictionary to map values to IDs
filtered3_data['ortsteil_id'] = filtered2_data['ortsteil'].map(ortsteil_dict) #function "map" takes keys as input and gives values as output


filtered4_data = filtered3_data[['ortsteil_id','ortsteil', 'name', 'wert', 'jahr']] #IMPORTANT: DO NOT FORGET TO DO DOUBLE SQUARE BRACKETS
# print(filtered3_data[['ortsteil', 'name', 'wert', 'jahr']])



# pivot the dataframe (in order to get information from "name"-column in several columns)
#take as new columns th stuff from column 'name', as new cell values take content of 'wert, do this for every diferent "ortsteil_id, ortsteil" combination
df_pivot = filtered4_data.pivot(index=['ortsteil_id','ortsteil'], columns='name', values='wert') #USEFUL PIVOT-function

# rename the index to match the original dataframe
#df_pivot = df_pivot.rename(index={0: 'ortsteil_id'})

# reset the index
df_pivot = df_pivot.reset_index()

#drop redundant column 'name'
#df_pivot2 = df_pivot.drop('name', axis=1)

#Renaming columns, left old, right new
df_pivot = df_pivot.rename(columns={ 'Kinder insgesamt': 'KitaKinder',
                                     'Straftaten insgesamt': 'Straftaten',
                                     '   mit Elektromotor': 'Elektroautos',
                                     'Lebenszufriedenheit': 'Lebenszufriedenheit_(Zufriedenheitsfaktor)',
                                     'Wohnviertel':'Wohnviertel_(Zufriedenheitsfaktor)',
                                     'Zukunftsaussicht':'Zukunftsaussicht_(Zufriedenheitsfaktor)',
                                     'Wirtschaftliche Lage': 'WirtschaftlicheLage_(Zufriedenheitsfaktor)',
                                     'ortsteil': 'Ortsteil',
                                     'ortsteil_id': 'Ortsteil_ID',
                                     'Durchschnittliche Haushaltsgröße':'DurchschnittlicheHaushaltsgröße',
                                     'Persönliches Einkommen':'PersönlichesEinkommen'
                                     })

columns = df_pivot.columns.tolist()
columns[2], columns[3] = columns[3], columns[2]
df_pivot = df_pivot[columns]


# Print the filtered data
#print(filtered4_data)

print()
#print(filtered4_data.to_string())
#print(df_pivot.shape)
#print(df_pivot.columns)

# print(df_pivot.to_string())  #dat hier

#print(filtered2_data['wert'].dtype)



"""
mat = filtered4_data.values
print(mat)
kmeans = KMeans(n_clusters=3) #create special instance
print(kmeans)
X = np.random.rand(100, 2)
# Fit the data to the KMeans model
kmeans.fit(X)

# Get the cluster labels for each data point
labels = kmeans.labels_

print(labels)

km = KMeans(n_clusters=5)
#km.fit(mat)
# Get cluster assignment labels
#labels = km.labels_
"""



print('----------------')
#print(df_pivot.to_string)
#print(df_pivot.dtypes)  #Before

for col in df_pivot.columns:
    try:
        #convert to string, then slice, then to float (before: values too long for float)
        if col != 'Ortsteil': # Ortsteile should not be shortened
            df_pivot[col] = df_pivot[col].astype(str)
            df_pivot[col] = df_pivot[col].str.slice(stop=7)
            df_pivot[col] = df_pivot[col].str.replace(',', '.').astype(float)
    except ValueError:
        pass

#print(df_pivot.dtypes) #After

print("--Datensatz vorbereitet--")

for col in df_pivot.columns:
    print(col)








