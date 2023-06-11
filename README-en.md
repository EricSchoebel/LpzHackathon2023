# Project for the Leipzig Open Data Hackathon 2023
## Topic: Artificial Intelligence for Urban Development
### MIRA - The AI Analysis Tool for the City of Leipzig

By Eric Schöbel

This project was created as part of the Leipzig Open Data Hackathon 2023. In response to the call initiated by the Office of Statistics and Elections of the City of Leipzig, Topic 1: "Artificial Intelligence for Urban Development" was chosen.

The project developed "MIRA" (Japanese for "mirror") is an AI analysis tool for the city of Leipzig. Based on unsupervised learning machine learning algorithms, real publicly available data for the Leipzig city area for the year 2021 can be evaluated live by the user. The web application program offers features for descriptive value comparison, clustering, and anomaly detection.

**Features**

In general, a dataset for the year 2021 is created, containing information about the 63 districts of Leipzig across 12 categories, such as the number of electric cars or the number of committed crimes. On the website, users can select the relevant districts and categories and receive real-time calculated results that can be analyzed as desired. The Leipzig Information System served as the data source.

1. Value Comparison

Under "Value Comparison," selected districts can be graphically visualized in a bar chart based on specific categories. This introductory feature provides an overview of the data and allows for descriptive comparisons.

2. Clustering

Under "Clustering," analysis can be performed to identify clusters of similar points among districts based on certain categories. The number of clusters can be manually chosen or optimized by the program. The results can be color-coded and graphically visualized if two categories are selected; otherwise, a textual output is provided. The underlying clustering algorithm used is K-Means from the field of partitioning cluster analysis.

3. Anomaly Detection

Under "Anomaly Detection," outliers in the data can be algorithmically identified. Similar to previous features, districts and categories can be selected, with a minimum of four districts required. If two categories are chosen, the results can be graphically visualized; otherwise, a textual output is provided. The underlying algorithm used is Local Outlier Factor (LOF) from the field of anomaly detection.

**Technical Details**

The *backend* was developed in Python using Flask. In addition to dataset preparation, it primarily executes machine learning algorithms from the Scikit-learn library. The results are provided to the frontend through an API. The *frontend* was built using Vue.js 3 with Vuetify 3.

To start the program in the backend, run the server by executing flask.py. Then, navigate to the frontend folder in the terminal and execute the frontend by running "npm run serve". Note that the necessary installations should be done beforehand.
The backend resolves cross-origin errors for requests from localhost:8080. To allow other addresses, the necessary adjustment can be made in flaskapp.py.

To get an impression of the web application, screenshots of the user interface can be viewed in the screenshot folder.

