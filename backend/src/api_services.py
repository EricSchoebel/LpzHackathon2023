# in here goes the acutal business logic / model
# -> functions that you call from the api_controller

from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from preparation import df_pivot
import pandas as pd

clean_df = df_pivot


def dataframe_to_dict(dataframe):
    # to_dict method of Pandas DataFrame is used to convert the DataFrame to a list of dictionaries,
    # where each dictionary represents a row in the DataFrame
    return dataframe.to_dict(orient='records')

def label_adder(dataframe, labels):
    df_copy = dataframe.copy()
    df_copy['label'] = labels #add labels column with result content
    return df_copy

#for ortsteile and kategorien decoding
def string_decoder(encoded_string): #decodes String to list of booleans
    boolean_list = [char == "1" for char in encoded_string]
    return boolean_list

def create_partial_rows_dataframe(dataframe, boolean_list):  #reduce rows
    new_df = dataframe.loc[boolean_list]
    return new_df

def create_partial_cols_dataframe(dataframe, boolean_list):  #reduce columns
    new_df = dataframe.loc[:, boolean_list]
    return new_df




def testing():
    test_dict = {
            'name': 'Herbert',
            'coolness': 19
            }
    return test_dict





#TAKEN FROM CALCULATION:

# k = number of clusters
# included_cols = which dimensions should be taken into account (maximum 12)
#   -> list of 1 (true) or 0 (false)
"""
first two categories are just Ortsteil_ID and Ortsteil. Then:
[Altenquote, Elektroautos, Altenquote, DurchschnittlicheHaushaltsgröße, Durchschnittsalter, Jugendquote, KitaKinder,
 Lebenszufriedenheit_(Zufriedenheitsfaktor), PersönlichesEinkommen, Straftaten,
  WirtschaftlicheLage_(Zufriedenheitsfaktor), Wohnviertel_(Zufriedenheitsfaktor), Zukunftsaussicht_(Zufriedenheitsfaktor)]
  
CAUTION: this is the ordering in the dataframe! It does not match the display in the API call
"""

def kmeansWithK(k, included_cols, dataframe):
    num_rows = dataframe.shape[0]
    if k>num_rows: #you cannot have more clusters the dataframe rows
        return None

    col_names = dataframe.columns.tolist() # get column names from DataFrame
    selected_cols = [col_names[i] for i, include in enumerate(included_cols) if include] # select relevant columns based on included_cols list
    X = dataframe[selected_cols].to_numpy()

    kmeans = KMeans(n_clusters=k, n_init='auto', init='k-means++')  # 'k-means++' selects initial centroids in a smart way
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

# LOF noch hier einfuegen!
# FIXME am Ende kann calculation.py vielleicht aufgeloest werden, wenn alle hier drin steht







