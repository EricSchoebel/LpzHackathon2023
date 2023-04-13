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
#import * from preparation

# clean_df = preparation.filtered4_data




import pandas as pd

# create sample data
data = {'ortsteil_id': [0, 0, 0, 0, 0, 0, 0],
        'ortsteil': ['Heiterblick', 'Heiterblick', 'Heiterblick', 'Heiterblick', 'Heiterblick', 'Heiterblick', 'Heiterblick'],
        'name': ['Kinder insgesamt', 'Lebenszufriedenheit', 'Wirtschaftliche Lage', 'Zukunftsaussicht', 'Wohnviertel', 'Straftaten insgesamt', 'Persönliches Einkommen'],
        'wert': [235, 2.2430623941, 2.098630266, 2.3588815305, 2.029225282, 355, 2000],
        'jahr': [2021, 2021, 2021, 2021, 2021, 2021, 2021]}

df = pd.DataFrame(data)

# pivot the dataframe
df_pivot = df.pivot(index='ortsteil_id', columns='name', values='wert')

# rename the index to match the original dataframe
df_pivot = df_pivot.rename(index={0: 'ortsteil_id'})

# reset the index
df_pivot = df_pivot.reset_index()

# display the resulting dataframe
print(df_pivot)
