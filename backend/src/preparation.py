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
# Load data from a JSON file
data = pd.read_json('files/json_files/a.json', orient='records')
data2 = pd.read_json('files/json_files/b.json', orient='records')
data3 = pd.read_json('files/json_files/c.json', orient='records')
data4 = pd.read_json('files/json_files/d.json', orient='records')
data5 = pd.read_json('files/json_files/e.json', orient='records')
data6 = pd.read_json('files/json_files/f.json', orient='records')
data7 = pd.read_json('files/json_files/g.json', orient='records')
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

print("alles ok")


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

#Renaming columns
df_pivot = df_pivot.rename(columns={ 'Kinder insgesamt': 'Kita-Kinder',
                                     'Straftaten insgesamt': 'Straftaten',
                                     '   mit Elektromotor': 'Elektroautos',
                                     'Lebenszufriedenheit': 'Lebenszufriedenheit (Zufriedenheitsfaktor)',
                                     'Wohnviertel':'Wohnviertel (Zufriedenheitsfaktor)',
                                     'Zukunftsaussicht':'Zukunftsaussicht (Zufriedenheitsfaktor)',
                                     'Wirtschaftliche Lage': 'Wirtschaftliche Lage (Zufriedenheitsfaktor)',
                                     'ortsteil': 'Ortsteil',
                                     'ortsteil_id': 'Ortsteil_ID'
                                     })

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
        df_pivot[col] = df_pivot[col].astype(str)
        df_pivot[col] = df_pivot[col].str.slice(stop=7)
        df_pivot[col] = df_pivot[col].str.replace(',', '.').astype(float)
    except ValueError:
        pass

#print(df_pivot.dtypes) #After



#ToDo: hier weitermachen, am besten eig in calculation.py

from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

clean_df = df_pivot

# Extract the numerical data from the DataFrame
#X = clean_df.select_dtypes(include=['float64', 'int64'])

#print(X)
#print(clean_df.to_string)

example = [False, False] + [True]*12
#example = [False, False] + [True]*10 + [False]*2




# k = number of clusters
# included_cols = which dimensions should be taken into account (maximum 12)
#   -> list of 1 (true) or 0 (false)
"""
[Elektroautos, Altenquote, Durchschnittliche Haushaltsgröße, Durchschnittsalter, Jugendquote, Kita-Kinder,
 Lebenszufriedenheit (Zufriedenheitsfaktor), Persönliches Einkommen, Straftaten,
  Wirtschaftliche Lage (Zufriedenheitsfaktor) Wohnviertel (Zufriedenheitsfaktor) Zukunftsaussicht (Zufriedenheitsfaktor)]
"""
def kmeansWithK(k, included_cols, dataframe):
    num_rows = dataframe.shape[0]
    if k>num_rows: #you cannot have more clusters the dataframe rows
        return None

    col_names = dataframe.columns.tolist() # get column names from DataFrame
    selected_cols = [col_names[i] for i, include in enumerate(included_cols) if include] # select relevant columns based on included_cols list
    X = dataframe[selected_cols].to_numpy()

    kmeans = KMeans(n_clusters=k, n_init='auto', init='k-means++')  # 'k-means++' selects initial centorids in a smart way
    kmeans.fit(X)
    return kmeans.labels_ #list of the labels

def kmeansWithoutK(included_cols, dataframe):
    k = determineOptimalK(included_cols, dataframe)
    return kmeansWithK(k, included_cols, dataframe)


#Using the silhouette score for determining the optimal number of clusters:
#The score is a measure of how similar an object is to its own cluster compared to other clusters.
#It takes values in the range of [-1, 1], where a higher score indicates better clustering performance.
#-> K-means clustering for different values of K (2 to 10) and compute the silhouette score for each clustering result
#-> select the K value with the highest silhouette score as the optimal number of clusters
def determineOptimalK(included_cols, dataframe):
    col_names = dataframe.columns.tolist()  # get column names from DataFrame
    selected_cols = [col_names[i] for i, include in enumerate(included_cols) if include]  # select relevant columns based on included_cols list
    X = dataframe[selected_cols].to_numpy()

    silhouette_scores = []
    for i in range(2, 11): # 2 included, 11 excluded
        kmeans = KMeans(n_clusters=i, n_init='auto', random_state=0) .fit(X)
        score = silhouette_score(X, kmeans.labels_)
        silhouette_scores.append(score)
    optimal_k = silhouette_scores.index(max(silhouette_scores)) + 2
    return optimal_k

"""
Further remarks (from https://scikit-learn.org/stable/modules/generated/sklearn.cluster.k_means.html)
'n_init': Number of time the k-means algorithm will be run with different centroid seeds kmeans
When n_init='auto', the number of runs depends on the value of init: 10 if using init='random', 1 if using init='k-means++'.
"""

#testing
print(kmeansWithK(2, example, clean_df))
print(kmeansWithoutK(example, clean_df))







