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


from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler
from preparation import df_pivot

clean_df = df_pivot #complete clean dataset
#pd.set_option('display.max_rows', None)
#pd.set_option('display.max_columns', None)
#print(clean_df.to_string)

# Extract the numerical data from the DataFrame
#X = clean_df.select_dtypes(include=['float64', 'int64'])

#print(X)
#print(clean_df.to_string)



def label_adder(dataframe, labels):
    df_copy = dataframe.copy()
    df_copy['label'] = labels #add labels column with result content
    return df_copy





import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import LocalOutlierFactor

np.random.seed(42)

example2 = [False, False] + [True]*12
#detect outliers with LOF (Local Outlier Factor)
def detectOutliersLOF(included_cols, dataframe):
    col_names = dataframe.columns.tolist()  # get column names from DataFrame
    selected_cols = [col_names[i] for i, include in enumerate(included_cols) if
                     include]  # select relevant columns based on included_cols list
    X = dataframe[selected_cols].to_numpy()

    # Check if it has more than 4 rows and more than 1 column
    if X.shape[0] <= 4 and X.shape[1] <= 1:
        return

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)  # Scale the data

    lof = LocalOutlierFactor(n_neighbors=20, contamination='auto', novelty=False)
    lof.fit(X_scaled)
    # Predict the outlier scores
    outlier_scores = lof.negative_outlier_factor_
    #print(outlier_scores)
    # Set a threshold for outlier detection
    threshold = -1.5
    # Generate labels (1 for outliers, 0 for inliers)
    labels = [1 if score < threshold else 0 for score in outlier_scores]

    return label_adder(dataframe, labels)




#print( detectOutliersLOF(example2, clean_df) )
detectOutliersLOF(example2, clean_df)








"""
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


"""
